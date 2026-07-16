import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "test-iframe-heights.py"


class IframeTesterCliTests(unittest.TestCase):
    def test_help_does_not_require_playwright(self):
        result = subprocess.run(
            [sys.executable, "-S", str(SCRIPT), "--help"],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--sims-dir", result.stdout)
        self.assertIn("--report", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_real_run_without_playwright_has_an_actionable_error(self):
        with tempfile.TemporaryDirectory() as temporary:
            sims = Path(temporary) / "sims"
            sims.mkdir()
            result = subprocess.run(
                [sys.executable, "-S", str(SCRIPT), "--sims-dir", str(sims)],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 2)
        self.assertIn("pip install playwright", result.stderr)
        self.assertIn("playwright install chromium", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_installed_playwright_contract_still_runs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sims = root / "sims"
            sims.mkdir()
            package = root / "playwright"
            package.mkdir()
            (package / "__init__.py").write_text("", encoding="utf-8")
            (package / "sync_api.py").write_text(
                textwrap.dedent(
                    """
                    class Browser:
                        def new_page(self):
                            return object()

                        def close(self):
                            pass


                    class Chromium:
                        def launch(self, headless=True):
                            return Browser()


                    class Driver:
                        chromium = Chromium()


                    class PlaywrightContext:
                        def __enter__(self):
                            return Driver()

                        def __exit__(self, exc_type, exc, traceback):
                            return False


                    def sync_playwright():
                        return PlaywrightContext()
                    """
                ).lstrip(),
                encoding="utf-8",
            )
            env = os.environ.copy()
            env["PYTHONPATH"] = str(root)
            result = subprocess.run(
                [sys.executable, "-S", str(SCRIPT), "--sims-dir", str(sims)],
                text=True,
                capture_output=True,
                check=False,
                env=env,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Testing 0 MicroSim(s)", result.stdout)
        self.assertIn("Total: 0", result.stdout)


if __name__ == "__main__":
    unittest.main()
