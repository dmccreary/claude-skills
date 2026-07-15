#!/usr/bin/env python3
"""Regression tests for supported intelligent-textbook source layouts."""

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("book-metrics.py")
SPEC = importlib.util.spec_from_file_location("book_metrics", MODULE_PATH)
BOOK_METRICS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BOOK_METRICS)
BookMetricsGenerator = BOOK_METRICS.BookMetricsGenerator


class LayoutDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.docs = Path(self.temp_dir.name) / "docs"
        (self.docs / "chapters").mkdir(parents=True)
        (self.docs / "learning-graph").mkdir(parents=True)

    def write(self, relative_path: str, content: str) -> Path:
        path = self.docs / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_directory_layout_remains_supported(self):
        self.write(
            "chapters/01-foundations/index.md",
            "# Foundations\n\n## First section\n\nUseful chapter text.\n",
        )
        self.write(
            "learning-graph/learning-graph.csv",
            "id,name\nconcept-1,First concept\n",
        )

        generator = BookMetricsGenerator(str(self.docs))
        count, chapters = generator.count_chapters()

        self.assertEqual(count, 1)
        self.assertEqual(chapters[0]["name"], "Foundations")
        self.assertEqual(chapters[0]["layout"], "directory")
        self.assertEqual(generator.count_concepts(), 1)
        self.assertIn(
            "../chapters/01-foundations/index.md",
            generator.generate_chapter_metrics_md(),
        )

    def test_flat_chapters_and_concepts_inventory_are_supported(self):
        self.write("chapters/index.md", "# Chapters\n")
        self.write(
            "chapters/01-outcomes.md",
            "# Outcomes\n\n## Define the result\n\nStart with the result and name a host plant.\n",
        )
        self.write(
            "chapters/02-evidence.md",
            "# Evidence\n\n## Inspect reality\n\nMeasure what happened.\n",
        )
        self.write(
            "learning-graph/concepts.csv",
            "id,name\nconcept-1,Outcome\nconcept-2,Evidence\n",
        )

        generator = BookMetricsGenerator(str(self.docs))
        count, chapters = generator.count_chapters()

        self.assertEqual(count, 2)
        self.assertEqual([chapter["number"] for chapter in chapters], [1, 2])
        self.assertTrue(all(chapter["layout"] == "flat-file" for chapter in chapters))
        self.assertEqual(generator.count_concepts(), 2)
        self.assertEqual(generator.count_host_plant_relationships(), 1)

        chapter_report = generator.generate_chapter_metrics_md()
        self.assertIn("../chapters/01-outcomes.md", chapter_report)
        self.assertIn("../chapters/02-evidence.md", chapter_report)
        self.assertNotIn("../chapters/index.md", chapter_report)

    def test_directory_layout_wins_when_the_same_chapter_also_has_a_flat_file(self):
        self.write("chapters/01-foundations.md", "# Flat duplicate\n")
        self.write("chapters/01-foundations/index.md", "# Canonical directory chapter\n")

        generator = BookMetricsGenerator(str(self.docs))
        count, chapters = generator.count_chapters()

        self.assertEqual(count, 1)
        self.assertEqual(chapters[0]["layout"], "directory")
        self.assertEqual(chapters[0]["name"], "Canonical directory chapter")

    def test_multiple_legacy_directories_with_the_same_prefix_are_not_collapsed(self):
        self.write("chapters/01-first/index.md", "# First directory chapter\n")
        self.write("chapters/01-second/index.md", "# Second directory chapter\n")

        generator = BookMetricsGenerator(str(self.docs))
        count, chapters = generator.count_chapters()

        self.assertEqual(count, 2)
        self.assertEqual(
            [chapter["name"] for chapter in chapters],
            ["First directory chapter", "Second directory chapter"],
        )

    def test_missing_h1_uses_a_layout_appropriate_fallback_title(self):
        self.write("chapters/01-directory/index.md", "No heading here.\n")
        self.write("chapters/02-flat-file.md", "No heading here either.\n")

        generator = BookMetricsGenerator(str(self.docs))
        _, chapters = generator.count_chapters()

        self.assertEqual(
            [chapter["name"] for chapter in chapters],
            ["01-directory", "02-flat-file"],
        )

    def test_learning_graph_csv_takes_precedence_when_both_inventories_exist(self):
        self.write(
            "learning-graph/learning-graph.csv",
            "id,name\nlegacy-1,Legacy concept\n",
        )
        self.write(
            "learning-graph/concepts.csv",
            "id,name\nnew-1,New concept\nnew-2,Another concept\n",
        )

        generator = BookMetricsGenerator(str(self.docs))

        self.assertEqual(generator.count_concepts(), 1)


if __name__ == "__main__":
    unittest.main()
