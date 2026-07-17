import hashlib
import importlib.util
import runpy
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "init_textbook.py"
TEMPLATE_ROOT = Path(__file__).parents[1] / "assets" / "init-textbook"
SPEC = importlib.util.spec_from_file_location("init_textbook", SCRIPT_PATH)
init_textbook = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = init_textbook
SPEC.loader.exec_module(init_textbook)


def arguments(project: Path, **overrides):
    values = {
        "project_dir": project,
        "site_name": "Builder's Guide & Atlas",
        "site_description": "A practical guide to agents, evidence & tests.",
        "site_author": "Yaniv Ben-Ami",
        "github_username": "yaniv256",
        "repo_name": "builder-atlas",
        "linkedin_url": "https://www.linkedin.com/in/yaniv-ben-ami-9208b9184/",
        "primary_color": "deep orange",
        "accent_color": "blue",
        "year": "2026",
    }
    values.update(overrides)
    return init_textbook.argparse.Namespace(**values)


def tree_snapshot(root: Path) -> tuple:
    entries = []
    for path in sorted(root.rglob("*")):
        relative = str(path.relative_to(root))
        stat = path.lstat()
        if path.is_symlink():
            entries.append((relative, "symlink", path.readlink(), stat.st_mode))
        elif path.is_dir():
            entries.append((relative, "directory", stat.st_mode))
        else:
            entries.append(
                (
                    relative,
                    "file",
                    hashlib.sha256(path.read_bytes()).hexdigest(),
                    stat.st_mode,
                )
            )
    return tuple(entries)


class InitTextbookTests(unittest.TestCase):
    def test_scaffold_copies_hidden_and_binary_assets_and_escapes_yaml(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(
                arguments(project, site_author="Yaniv O'Ben-Ami")
            )

            paths = init_textbook.scaffold(config)

            self.assertIn(project / ".gitignore", paths)
            self.assertTrue((project / ".gitignore").is_file())
            self.assertTrue((project / "builder-atlas.code-workspace").is_file())
            self.assertTrue((project / "docs" / "js").is_dir())
            self.assertEqual(
                (project / "docs" / "img" / "cover.png").read_bytes(),
                (TEMPLATE_ROOT / "docs" / "img" / "cover.png").read_bytes(),
            )
            mkdocs = (project / "mkdocs.yml").read_text(encoding="utf-8")
            index = (project / "docs" / "index.md").read_text(encoding="utf-8")
            self.assertIn("site_name: 'Builder''s Guide & Atlas'", mkdocs)
            self.assertIn("site_author: 'Yaniv O''Ben-Ami'", mkdocs)
            self.assertIn("2026 Yaniv O''Ben-Ami. Licensed", mkdocs)
            self.assertIn("title: 'Builder''s Guide & Atlas'", index)
            self.assertIn("edit_uri: 'edit/main/docs/'", mkdocs)
            self.assertNotRegex(
                "\n".join(
                    path.read_text(encoding="utf-8")
                    for path in project.rglob("*")
                    if path.is_file() and path.suffix != ".png"
                ),
                init_textbook.TOKEN_PATTERN,
            )

    def test_collision_fails_before_any_output_is_written(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            existing = project / ".gitignore"
            existing.write_text("keep-me\n", encoding="utf-8")
            before = tree_snapshot(project)
            config = init_textbook.build_config(arguments(project))

            with self.assertRaisesRegex(
                init_textbook.ScaffoldError, "refusing to overwrite"
            ):
                init_textbook.scaffold(config)

            self.assertEqual(tree_snapshot(project), before)
            self.assertFalse((project / "mkdocs.yml").exists())

    def test_dry_run_validates_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))

            paths = init_textbook.scaffold(config, dry_run=True)

            self.assertGreater(len(paths), 10)
            self.assertEqual(list(project.iterdir()), [])

    def test_preview_uses_system_temp_and_write_cleans_descriptor_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            real_temporary_directory = tempfile.TemporaryDirectory
            stage_parents = []

            def capture_stage_parent(*args, **kwargs):
                stage_parents.append(kwargs.get("dir"))
                return real_temporary_directory(*args, **kwargs)

            with mock.patch.object(
                init_textbook.tempfile,
                "TemporaryDirectory",
                side_effect=capture_stage_parent,
            ):
                init_textbook.scaffold(config, dry_run=True)
                init_textbook.scaffold(config)

            self.assertEqual(stage_parents, [None])
            self.assertFalse(
                any(
                    path.name.startswith(".init-textbook-")
                    for path in project.iterdir()
                )
            )

    def test_write_failure_rolls_back_files_and_created_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            calls = 0

            real_copy = init_textbook.shutil.copyfileobj

            def fail_second_copy(source, destination):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("injected write failure")
                return real_copy(source, destination)

            with mock.patch.object(
                init_textbook.shutil, "copyfileobj", side_effect=fail_second_copy
            ):
                with self.assertRaisesRegex(
                    init_textbook.ScaffoldError, "injected write failure"
                ):
                    init_textbook.scaffold(config)

            self.assertEqual(list(project.iterdir()), [])

    def test_commit_does_not_overwrite_destination_created_after_preflight(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            init_textbook.preflight(config)

            with tempfile.TemporaryDirectory(dir=project.parent) as stage_dir:
                stage = Path(stage_dir)
                relative_paths = init_textbook.render_stage(config, stage)
                raced_destination = project / ".gitignore"
                raced_destination.write_text("created concurrently\n", encoding="utf-8")
                root_fd = init_textbook.open_project_directory(config)
                directory_fds, directory_identities = (
                    init_textbook.pin_output_directories(
                        config,
                        root_fd,
                        init_textbook.planned_destinations(config),
                    )
                )

                try:
                    with self.assertRaises(init_textbook.ScaffoldError):
                        init_textbook.commit_stage(
                            config,
                            stage,
                            relative_paths,
                            root_fd,
                            directory_fds,
                            directory_identities,
                        )
                finally:
                    for relative, fd in reversed(list(directory_fds.items())):
                        if relative != Path("."):
                            init_textbook.os.close(fd)
                    init_textbook.os.close(root_fd)

            self.assertEqual(
                raced_destination.read_text(encoding="utf-8"),
                "created concurrently\n",
            )
            self.assertEqual([path.name for path in project.iterdir()], [".gitignore"])

    def test_parent_swap_is_detected_without_writing_through_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            outside = Path(directory) / "outside"
            project.mkdir()
            outside.mkdir()
            config = init_textbook.build_config(arguments(project))
            real_open = init_textbook.os.open
            swapped = False

            def swap_parent_before_leaf(path, flags, mode=0o777, *, dir_fd=None):
                nonlocal swapped
                if path == "about.md" and dir_fd is not None and not swapped:
                    swapped = True
                    (project / "docs").rename(project / "docs-original")
                    (project / "docs").symlink_to(outside, target_is_directory=True)
                return real_open(path, flags, mode, dir_fd=dir_fd)

            with mock.patch.object(
                init_textbook.os, "open", side_effect=swap_parent_before_leaf
            ):
                with self.assertRaisesRegex(
                    init_textbook.ScaffoldError, "directory became unsafe"
                ):
                    init_textbook.scaffold(config)

            self.assertEqual(list(outside.iterdir()), [])
            self.assertFalse(any((project / "docs-original").rglob("*")))

    def test_project_ancestor_swap_is_rejected_before_staging(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "parent"
            project = parent / "project"
            replacement = root / "replacement"
            project.mkdir(parents=True)
            (replacement / "project").mkdir(parents=True)
            config = init_textbook.build_config(arguments(project))

            parent.rename(root / "original-parent")
            parent.symlink_to(replacement, target_is_directory=True)

            with self.assertRaisesRegex(
                init_textbook.ScaffoldError, "(?:changed|unsafe) before publication"
            ):
                init_textbook.scaffold(config)

            self.assertEqual(list((replacement / "project").iterdir()), [])
            self.assertEqual(list((root / "original-parent" / "project").iterdir()), [])

    def test_stage_directory_rebinding_is_rejected_before_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            real_render_stage = init_textbook.render_stage
            replacement_marker = "attacker-owned\n"

            def replace_stage_entry(render_config, stage):
                stage = Path(stage)
                try:
                    resolved_stage = Path(init_textbook.os.readlink(stage))
                except OSError:
                    resolved_stage = (
                        Path(init_textbook.os.readlink(stage.parent)) / stage.name
                    )
                moved_stage = resolved_stage.with_name(f"{resolved_stage.name}-moved")
                resolved_stage.rename(moved_stage)
                resolved_stage.mkdir()
                (resolved_stage / "marker.txt").write_text(
                    replacement_marker, encoding="utf-8"
                )
                return real_render_stage(render_config, stage)

            with mock.patch.object(
                init_textbook,
                "render_stage",
                side_effect=replace_stage_entry,
            ):
                with self.assertRaisesRegex(
                    init_textbook.ScaffoldError,
                    "staging directory changed before publication",
                ):
                    init_textbook.scaffold(config)

            self.assertFalse((project / "mkdocs.yml").exists())
            self.assertEqual(
                next(project.glob(".init-textbook-*/marker.txt")).read_text(
                    encoding="utf-8"
                ),
                replacement_marker,
            )

    def test_output_parent_created_after_pinning_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            destinations = init_textbook.preflight(config)
            root_fd = init_textbook.open_project_directory(config)
            directory_fds, directory_identities = init_textbook.pin_output_directories(
                config,
                root_fd,
                destinations,
            )

            with tempfile.TemporaryDirectory() as stage_directory:
                stage = Path(stage_directory)
                relative_paths = init_textbook.render_stage(config, stage)
                raced_parent = project / "docs"
                raced_parent.mkdir()
                marker = raced_parent / "marker.txt"
                marker.write_text("attacker-owned\n", encoding="utf-8")

                try:
                    with self.assertRaisesRegex(
                        init_textbook.ScaffoldError,
                        "output directory appeared after pinning: docs",
                    ):
                        init_textbook.commit_stage(
                            config,
                            stage,
                            relative_paths,
                            root_fd,
                            directory_fds,
                            directory_identities,
                        )
                finally:
                    for relative, fd in reversed(list(directory_fds.items())):
                        if relative != Path("."):
                            init_textbook.os.close(fd)
                    init_textbook.os.close(root_fd)

            self.assertEqual(marker.read_text(encoding="utf-8"), "attacker-owned\n")
            self.assertEqual(
                sorted(path.name for path in project.iterdir()),
                ["docs"],
            )

    def test_inserted_placeholder_text_is_not_substituted_again(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(
                arguments(project, site_name="{{SITE_AUTHOR}}")
            )

            with self.assertRaisesRegex(
                init_textbook.ScaffoldError,
                "unresolved placeholders",
            ):
                init_textbook.scaffold(config)

            self.assertEqual(list(project.iterdir()), [])

    def test_rollback_reports_cleanup_failures_and_preserves_primary_error(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            config = init_textbook.build_config(arguments(project))
            real_copy = init_textbook.shutil.copyfileobj
            real_unlink = init_textbook.os.unlink
            copies = 0
            unlinks = 0

            def fail_second_copy(source, destination):
                nonlocal copies
                copies += 1
                if copies == 2:
                    raise OSError("primary copy failure")
                return real_copy(source, destination)

            def fail_first_unlink(path, *, dir_fd=None):
                nonlocal unlinks
                unlinks += 1
                if unlinks == 1:
                    raise OSError("rollback unlink failure")
                return real_unlink(path, dir_fd=dir_fd)

            with (
                mock.patch.object(
                    init_textbook.shutil, "copyfileobj", side_effect=fail_second_copy
                ),
                mock.patch.object(
                    init_textbook.os, "unlink", side_effect=fail_first_unlink
                ),
            ):
                with self.assertRaisesRegex(
                    init_textbook.ScaffoldError,
                    "primary copy failure.*rollback failures.*rollback unlink failure",
                ):
                    init_textbook.scaffold(config)

            self.assertTrue((project / "docs" / "about.md").exists())

    def test_rejects_github_username_with_consecutive_hyphens(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            with self.assertRaisesRegex(
                init_textbook.ScaffoldError, "valid GitHub account"
            ):
                init_textbook.build_config(
                    arguments(project, github_username="foo--bar")
                )

    def test_invalid_metadata_fails_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)

            with self.assertRaisesRegex(init_textbook.ScaffoldError, "single line"):
                init_textbook.build_config(
                    arguments(project, site_description="first line\nsecond line")
                )

            self.assertEqual(list(project.iterdir()), [])

    def test_help_is_non_mutating(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            result = subprocess.run(
                [sys.executable, str(SCRIPT_PATH), "--help"],
                cwd=project,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("--dry-run", result.stdout)
            self.assertEqual(list(project.iterdir()), [])

    def test_template_comment_matches_explicit_image_only_hook(self):
        mkdocs = (TEMPLATE_ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        hook_path = TEMPLATE_ROOT / "plugins" / "social_override.py"
        hook = runpy.run_path(str(hook_path))

        self.assertIn("overrides og:image and twitter:image only when", mkdocs)
        self.assertIn("a page explicitly declares `image:`", mkdocs)
        self.assertNotIn("falling back to the site-", mkdocs)
        html = '<html><head><meta property="og:image" content="old"></head></html>'
        no_image_page = types.SimpleNamespace(meta={})
        image_page = types.SimpleNamespace(meta={"image": "img/cover.png"})
        config = {"site_url": "https://example.com/book/"}
        self.assertEqual(hook["on_post_page"](html, no_image_page, config), html)
        rendered = hook["on_post_page"](html, image_page, config)
        expected = "https://example.com/book/img/cover.png"
        self.assertIn(f'property="og:image" content="{expected}"', rendered)
        self.assertIn(f'name="twitter:image" content="{expected}"', rendered)

    def test_manifest_covers_the_complete_canonical_template(self):
        actual = {
            path.relative_to(TEMPLATE_ROOT)
            for path in TEMPLATE_ROOT.rglob("*")
            if path.is_file()
        }
        self.assertEqual(init_textbook.REQUIRED_TEMPLATES, actual)
        self.assertEqual(
            init_textbook.BINARY_TEMPLATES,
            {Path("docs/img/cover.png"), Path("docs/img/license.png")},
        )


if __name__ == "__main__":
    unittest.main()
