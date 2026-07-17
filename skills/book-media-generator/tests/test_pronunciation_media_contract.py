#!/usr/bin/env python3
"""Contract tests for the active pronunciation publication route."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_ROOT / "scripts" / "audio" / "generate-pronunciation.py"
GUIDE_PATH = SKILL_ROOT / "references" / "pronounce-button-guide.md"
CONTROLLER_PATH = (
    SKILL_ROOT / "assets" / "pronunciation" / "pronunciation-controls.js"
)


def load_module():
    spec = importlib.util.spec_from_file_location("generate_pronunciation", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class FakeResponse:
    def __init__(self, body: bytes, headers: dict[str, str] | None = None):
        self.body = body
        self.headers = headers or {"Content-Type": "audio/mpeg"}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, size=-1):
        return self.body if size < 0 else self.body[:size]


class InterruptedResponse(FakeResponse):
    def read(self, size=-1):
        raise OSError("connection interrupted")


class PronunciationGeneratorContractTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.env = mock.patch.dict(os.environ, {"ELEVENLABS_API_KEY": "test-key"})
        self.env.start()
        self.addCleanup(self.env.stop)

    def generate_with(self, response, output: Path, **kwargs):
        output_root = kwargs.pop("output_root", output.parent or Path.cwd())
        with mock.patch.object(self.module.urllib.request, "urlopen", return_value=response):
            return self.module.generate_pronunciation(
                "Pareto",
                str(output),
                output_root=output_root,
                **kwargs,
            )

    def test_basename_output_is_supported(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            previous = Path.cwd()
            os.chdir(temp_dir)
            self.addCleanup(os.chdir, previous)
            self.generate_with(FakeResponse(b"ID3\x04\x00\x00audio"), Path("pareto.mp3"))
            self.assertTrue(Path("pareto.mp3").is_file())

    def test_slugify_cannot_emit_path_syntax(self):
        self.assertEqual(self.module.slugify("../escape"), "escape")
        self.assertEqual(self.module.slugify("A/B Test"), "a-b-test")
        for term in ("../escape", "A/B Test", r"A\\B Test"):
            slug = self.module.slugify(term)
            self.assertNotIn("/", slug)
            self.assertNotIn("\\", slug)
            self.assertNotIn("..", slug)

    def test_output_cannot_escape_approved_root(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "approved"
            root.mkdir()
            with self.assertRaises(ValueError):
                self.module.resolve_output_path("../escape.mp3", root)
            self.assertFalse((Path(temp_dir) / "escape.mp3").exists())

    def test_invalid_success_body_is_not_published(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            with self.assertRaises(ValueError):
                self.generate_with(
                    FakeResponse(
                        b'{"detail":"quota exceeded"}',
                        {"Content-Type": "application/json"},
                    ),
                    output,
                )
            self.assertFalse(output.exists())

    def test_oversized_success_body_is_not_published(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            with mock.patch.object(self.module, "MAX_AUDIO_BYTES", 8):
                with self.assertRaises(ValueError):
                    self.generate_with(
                        FakeResponse(b"ID3\x04\x00\x00oversized"), output
                    )
            self.assertFalse(output.exists())

    def test_interrupted_read_preserves_existing_artifact(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            output.write_bytes(b"existing-audio")
            with self.assertRaises(OSError):
                self.generate_with(InterruptedResponse(b""), output, force=True)
            self.assertEqual(output.read_bytes(), b"existing-audio")

    def test_success_records_artifact_provenance(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            self.generate_with(
                FakeResponse(
                    b"ID3\x04\x00\x00audio",
                    {
                        "Content-Type": "audio/mpeg",
                        "request-id": "request-123",
                        "x-trace-id": "trace-456",
                    },
                ),
                output,
            )
            provenance_path = Path(f"{output}.json")
            provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
            self.assertEqual(provenance["request_id"], "request-123")
            self.assertEqual(provenance["trace_id"], "trace-456")
            self.assertEqual(provenance["term"], "Pareto")
            self.assertEqual(provenance["output_format"], "mp3_44100_128")
            self.assertEqual(
                provenance["audio_sha256"],
                self.module.hashlib.sha256(output.read_bytes()).hexdigest(),
            )

    def test_request_pins_format_model_and_audio_accept_header(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            with mock.patch.object(
                self.module.urllib.request,
                "urlopen",
                return_value=FakeResponse(b"ID3\x04\x00\x00audio"),
            ) as urlopen:
                self.module.generate_pronunciation(
                    "Pareto", str(output), output_root=output.parent
                )
            request = urlopen.call_args.args[0]
            payload = json.loads(request.data.decode("utf-8"))
            self.assertIn("output_format=mp3_44100_128", request.full_url)
            self.assertEqual(payload["model_id"], "eleven_multilingual_v2")
            self.assertEqual(request.headers["Accept"], "audio/mpeg")
            self.assertEqual(
                urlopen.call_args.kwargs["timeout"],
                self.module.REQUEST_TIMEOUT_SECONDS,
            )

    def test_matching_artifact_is_reused_without_api_call(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            self.generate_with(FakeResponse(b"ID3\x04\x00\x00audio"), output)
            with mock.patch.object(
                self.module.urllib.request,
                "urlopen",
                side_effect=AssertionError("matching artifact should not call the API"),
            ):
                reused = self.module.generate_pronunciation(
                    "Pareto", str(output), output_root=output.parent
                )
            self.assertEqual(reused["term"], "Pareto")

    def test_nonmatching_existing_artifact_requires_force(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            output.write_bytes(b"existing-audio")
            with self.assertRaises(FileExistsError):
                self.generate_with(FakeResponse(b"ID3\x04\x00\x00new"), output)
            self.assertEqual(output.read_bytes(), b"existing-audio")

    def test_success_leaves_no_staging_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            self.generate_with(FakeResponse(b"ID3\x04\x00\x00audio"), output)
            leftovers = list(output.parent.glob(".*.tmp"))
            self.assertEqual(leftovers, [])

    def test_provenance_replace_failure_restores_existing_pair(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "pareto.mp3"
            provenance_path = Path(f"{output}.json")
            output.write_bytes(b"existing-audio")
            provenance_path.write_text('{"existing": true}\n', encoding="utf-8")
            original_audio = output.read_bytes()
            original_provenance = provenance_path.read_bytes()
            real_replace = self.module.os.replace
            replace_count = 0

            def fail_second_replace(source, destination):
                nonlocal replace_count
                replace_count += 1
                if replace_count == 2:
                    raise OSError("provenance replacement failed")
                return real_replace(source, destination)

            with mock.patch.object(
                self.module.os, "replace", side_effect=fail_second_replace
            ):
                with self.assertRaises(OSError):
                    self.generate_with(
                        FakeResponse(b"ID3\x04\x00\x00replacement"),
                        output,
                        force=True,
                    )

            self.assertEqual(output.read_bytes(), original_audio)
            self.assertEqual(provenance_path.read_bytes(), original_provenance)
            self.assertEqual(list(output.parent.glob(".*.tmp")), [])


class PronunciationGuideContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guide = GUIDE_PATH.read_text(encoding="utf-8")

    def test_guide_has_no_private_machine_prerequisite(self):
        self.assertNotIn("/Users/", self.guide)

    def test_guide_requires_current_capability_discovery(self):
        for required in (
            "GET /v1/models",
            "GET /v2/voices",
            "output_format",
            "request-id",
            "pronunciation_dictionary_locators",
        ):
            with self.subTest(required=required):
                self.assertIn(required, self.guide)

    def test_markup_is_csp_compatible_and_accessible(self):
        self.assertNotIn("onclick=", self.guide)
        self.assertIn("<audio", self.guide)
        self.assertIn(" controls", self.guide)
        self.assertIn("aria-label=", self.guide)
        self.assertIn('role="status"', self.guide)
        self.assertIn("addEventListener", self.guide)

    def test_external_controller_has_no_inline_handler_dependency(self):
        controller = CONTROLLER_PATH.read_text(encoding="utf-8")
        self.assertIn("DOMContentLoaded", controller)
        self.assertIn("addEventListener('error'", controller)
        self.assertIn("Pronunciation unavailable", controller)
        self.assertNotIn("innerHTML", controller)


if __name__ == "__main__":
    unittest.main()
