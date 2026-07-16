import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate-microsim-index.py"


def digest_tree(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def make_project(root: Path) -> None:
    (root / "mkdocs.yml").write_text("site_name: Decision Lab\n", encoding="utf-8")
    sims = root / "docs" / "sims"
    (sims / "alpha").mkdir(parents=True)
    (sims / "alpha" / "main.html").write_text("<main>Alpha</main>\n", encoding="utf-8")
    (sims / "alpha" / "index.md").write_text(
        "---\ntitle: Alpha Tool\n---\n\n# Alpha Tool\n", encoding="utf-8"
    )
    (sims / "beta").mkdir()
    (sims / "beta" / "main.html").write_text("<main>Beta</main>\n", encoding="utf-8")
    (sims / "beta" / "index.md").write_text(
        "---\ntitle: Beta Tool\ndescription: Compare two options.\n---\n\n# Beta Tool\n",
        encoding="utf-8",
    )
    (sims / "beta" / "beta.png").write_bytes(b"PNG")
    (sims / "shared").mkdir()
    (sims / "shared" / "index.md").write_text("# Shared support\n", encoding="utf-8")
    (sims / "index.md").write_text("original index\n", encoding="utf-8")
    (sims / "TODO.md").write_text("original todo\n", encoding="utf-8")


class MicroSimIndexCliTests(unittest.TestCase):
    def test_help_is_byte_clean_from_a_project_working_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_project(root)
            before = digest_tree(root)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--help"],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("--project-dir", result.stdout)
            self.assertIn("--dry-run", result.stdout)
            self.assertEqual(digest_tree(root), before)

    def test_dry_run_reports_without_writing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_project(root)
            before = digest_tree(root)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-dir", str(root), "--dry-run"],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Would process 2 MicroSims", result.stdout)
            self.assertIn("Missing screenshots: 1", result.stdout)
            self.assertIn("Descriptions to add: 1", result.stdout)
            self.assertEqual(digest_tree(root), before)

    def test_explicit_run_generates_the_catalog_and_todo(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_project(root)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-dir", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            index = (root / "docs" / "sims" / "index.md").read_text(encoding="utf-8")
            todo = (root / "docs" / "sims" / "TODO.md").read_text(encoding="utf-8")
            alpha = (root / "docs" / "sims" / "alpha" / "index.md").read_text(encoding="utf-8")
            self.assertIn("List of MicroSims for Decision Lab", index)
            self.assertLess(index.index("Alpha Tool"), index.index("Beta Tool"))
            self.assertNotIn("shared", index)
            self.assertIn("bk-capture-screenshot docs/sims/alpha", todo)
            self.assertNotIn("docs/sims/beta", todo)
            self.assertIn("description: Interactive MicroSim for alpha tool.", alpha)

    def test_explicit_run_catalogs_a_page_without_frontmatter_without_rewriting_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_project(root)
            gamma = root / "docs" / "sims" / "gamma"
            gamma.mkdir()
            (gamma / "main.html").write_text("<main>Gamma</main>\n", encoding="utf-8")
            index_path = gamma / "index.md"
            index_path.write_text("# Gamma Tool\n", encoding="utf-8")
            before = index_path.read_bytes()

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-dir", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = (root / "docs" / "sims" / "index.md").read_text(encoding="utf-8")
            self.assertIn("Gamma Tool", catalog)
            self.assertEqual(index_path.read_bytes(), before)

    def test_invalid_project_root_fails_without_writing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            before = digest_tree(root)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-dir", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must contain mkdocs.yml", result.stderr)
            self.assertEqual(digest_tree(root), before)


if __name__ == "__main__":
    unittest.main()
