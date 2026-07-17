#!/usr/bin/env python3
"""Generate a validated MP3 pronunciation artifact with provenance."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
DEFAULT_MODEL_ID = "eleven_multilingual_v2"
PHONEME_MODEL_ID = "eleven_flash_v2"
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"
MP3_CONTENT_TYPES = {"audio/mpeg", "audio/mp3"}
REQUEST_TIMEOUT_SECONDS = 60
MAX_AUDIO_BYTES = 16 * 1024 * 1024
MAX_ERROR_BYTES = 64 * 1024


def slugify(term: str) -> str:
    """Convert a term to one non-empty filename component."""
    slug = re.sub(r"[^a-z0-9]+", "-", term.casefold()).strip("-")
    if not slug:
        raise ValueError("Term does not contain a filename-safe character")
    return slug


def resolve_output_path(output_path: str, output_root: str | Path = ".") -> Path:
    """Resolve one MP3 path beneath an explicitly approved root."""
    root = Path(output_root).expanduser().resolve()
    candidate = Path(output_path).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ValueError(f"Output must stay beneath {root}: {output_path}") from error
    if resolved.suffix.casefold() != ".mp3":
        raise ValueError("Output path must end in .mp3")
    resolved.parent.mkdir(parents=True, exist_ok=True)
    return resolved


def _header(headers, name: str) -> str | None:
    if headers is None:
        return None
    if hasattr(headers, "get"):
        value = headers.get(name)
        if value is not None:
            return str(value)
    for key, value in getattr(headers, "items", lambda: [])():
        if str(key).casefold() == name.casefold():
            return str(value)
    return None


def _is_mp3(data: bytes) -> bool:
    return len(data) >= 4 and (
        data.startswith(b"ID3") or (data[0] == 0xFF and data[1] & 0xE0 == 0xE0)
    )


def _stage_bytes(destination: Path, data: bytes) -> Path:
    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return temporary_path


def _publish_artifact_pair(
    audio_path: Path,
    audio_stage: Path,
    provenance_path: Path,
    provenance_stage: Path,
) -> None:
    """Publish audio and provenance together, restoring the old pair on error."""
    publications = (
        (audio_path, audio_stage),
        (provenance_path, provenance_stage),
    )
    backups: dict[Path, Path] = {}
    try:
        for destination, _ in publications:
            if destination.exists():
                if not destination.is_file():
                    raise IsADirectoryError(f"Artifact destination is not a file: {destination}")
                backups[destination] = _stage_bytes(
                    destination, destination.read_bytes()
                )
    except BaseException:
        for backup in backups.values():
            backup.unlink(missing_ok=True)
        raise

    retain_backups = False
    try:
        for destination, staged in publications:
            os.replace(staged, destination)
    except BaseException as publication_error:
        rollback_errors = []
        for destination, _ in reversed(publications):
            try:
                backup = backups.get(destination)
                if backup is not None:
                    os.replace(backup, destination)
                else:
                    destination.unlink(missing_ok=True)
            except OSError as rollback_error:
                rollback_errors.append(f"{destination}: {rollback_error}")
        if rollback_errors:
            retain_backups = True
            retained = ", ".join(
                str(path) for path in backups.values() if path.exists()
            ) or "none"
            raise RuntimeError(
                "Artifact publication failed and rollback could not be verified; "
                f"retained backups: {retained}; rollback errors: "
                + "; ".join(rollback_errors)
            ) from publication_error
        raise
    finally:
        if not retain_backups:
            for backup in backups.values():
                backup.unlink(missing_ok=True)


def _request_fingerprint(request_contract: dict) -> str:
    encoded = json.dumps(
        request_contract, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _matching_artifact(output_path: Path, provenance_path: Path, fingerprint: str):
    if not output_path.is_file() or not provenance_path.is_file():
        return None
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if provenance.get("request_sha256") != fingerprint:
        return None
    if provenance.get("audio_sha256") != hashlib.sha256(output_path.read_bytes()).hexdigest():
        return None
    return provenance


def generate_pronunciation(
    term: str,
    output_path: str,
    voice_id: str = DEFAULT_VOICE_ID,
    ssml_arpabet: str | None = None,
    *,
    model_id: str | None = None,
    output_format: str = DEFAULT_OUTPUT_FORMAT,
    output_root: str | Path = ".",
    force: bool = False,
):
    """Generate, validate, and atomically publish an MP3 plus JSON provenance."""
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("ELEVENLABS_API_KEY environment variable is not set")

    resolved_output = resolve_output_path(output_path, output_root)
    provenance_path = Path(f"{resolved_output}.json")
    selected_model = model_id or (PHONEME_MODEL_ID if ssml_arpabet else DEFAULT_MODEL_ID)

    if ssml_arpabet:
        if not re.fullmatch(r"[A-Z0-9 ]+", ssml_arpabet):
            raise ValueError("CMU Arpabet may contain only A-Z, digits, and spaces")
        text = (
            f'<phoneme alphabet="cmu-arpabet" ph="{ssml_arpabet}">'
            f"{html.escape(term)}</phoneme>"
        )
    else:
        text = term

    request_contract = {
        "term": term,
        "text": text,
        "voice_id": voice_id,
        "model_id": selected_model,
        "output_format": output_format,
        "ssml_arpabet": ssml_arpabet,
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8,
            "style": 0.0,
            "speed": 0.9,
        },
    }
    fingerprint = _request_fingerprint(request_contract)
    existing = _matching_artifact(resolved_output, provenance_path, fingerprint)
    if existing and not force:
        print(f"Reused: {resolved_output}  [{selected_model}]")
        return existing
    if (resolved_output.exists() or provenance_path.exists()) and not force:
        raise FileExistsError(
            f"Existing artifact does not match this request: {resolved_output}; use --force"
        )

    query = urllib.parse.urlencode({"output_format": output_format})
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?{query}"
    payload = json.dumps(
        {
            "text": text,
            "model_id": selected_model,
            "voice_settings": request_contract["voice_settings"],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(
            request, timeout=REQUEST_TIMEOUT_SECONDS
        ) as response:
            audio = response.read(MAX_AUDIO_BYTES + 1)
            content_type = (_header(response.headers, "Content-Type") or "").split(";", 1)[0].casefold()
            request_id = _header(response.headers, "request-id")
            trace_id = _header(response.headers, "x-trace-id")
    except urllib.error.HTTPError as error:
        body = error.read(MAX_ERROR_BYTES).decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs HTTP {error.code}: {body}") from error

    if len(audio) > MAX_AUDIO_BYTES:
        raise ValueError(f"Response exceeds {MAX_AUDIO_BYTES} byte pronunciation limit")
    if content_type not in MP3_CONTENT_TYPES:
        raise ValueError(f"Expected audio/mpeg response, received {content_type or 'no Content-Type'}")
    if not _is_mp3(audio):
        raise ValueError("Response body is not recognizable MP3 data")

    provenance = {
        **request_contract,
        "request_sha256": fingerprint,
        "audio_sha256": hashlib.sha256(audio).hexdigest(),
        "bytes": len(audio),
        "content_type": content_type,
        "request_id": request_id,
        "trace_id": trace_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    audio_stage = _stage_bytes(resolved_output, audio)
    provenance_stage = _stage_bytes(
        provenance_path,
        (json.dumps(provenance, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )
    try:
        _publish_artifact_pair(
            resolved_output,
            audio_stage,
            provenance_path,
            provenance_stage,
        )
    finally:
        audio_stage.unlink(missing_ok=True)
        provenance_stage.unlink(missing_ok=True)

    print(f"Generated: {resolved_output}  [{selected_model}; {output_format}]")
    return provenance


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a validated MP3 pronunciation via ElevenLabs TTS"
    )
    parser.add_argument("term", help="The term to pronounce")
    parser.add_argument("--output", "-o", help="Output MP3 path beneath --output-root")
    parser.add_argument("--output-root", default=".", help="Approved output root (default: current directory)")
    parser.add_argument("--voice-id", default=DEFAULT_VOICE_ID)
    parser.add_argument("--model-id", default=None, help="Verified text-to-speech model ID")
    parser.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT)
    parser.add_argument("--force", action="store_true", help="Replace a non-matching existing artifact")
    parser.add_argument(
        "--ssml",
        dest="ssml_arpabet",
        default=None,
        help="CMU Arpabet phonemes; defaults the model to eleven_flash_v2",
    )
    args = parser.parse_args()

    output_path = args.output or f"docs/audio/{slugify(args.term)}.mp3"
    try:
        generate_pronunciation(
            args.term,
            output_path,
            args.voice_id,
            args.ssml_arpabet,
            model_id=args.model_id,
            output_format=args.output_format,
            output_root=args.output_root,
            force=args.force,
        )
    except (OSError, RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
