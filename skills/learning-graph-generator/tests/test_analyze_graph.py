import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "analyze-graph.py"
spec = importlib.util.spec_from_file_location("analyze_graph", SCRIPT)
analyze_graph = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(analyze_graph)


def write_graph(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "ConceptID",
                "ConceptLabel",
                "Dependencies",
                "TaxonomyID",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


class AnalyzeGraphTests(unittest.TestCase):
    def generate(self, rows: list[dict[str, str]]) -> str:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            graph_path = root / "graph.csv"
            report_path = root / "report.md"
            write_graph(graph_path, rows)
            analyze_graph.generate_report(str(graph_path), str(report_path))
            return report_path.read_text(encoding="utf-8")

    def test_self_dependency_is_reported_without_recursion_error(self):
        report = self.generate(
            [
                {
                    "ConceptID": "1",
                    "ConceptLabel": "Self Edge",
                    "Dependencies": "1",
                    "TaxonomyID": "TEST",
                }
            ]
        )

        self.assertIn("**Valid DAG Structure**: ❌ No", report)
        self.assertIn("**Self-Dependencies**: ❌ 1 detected", report)
        self.assertIn("**1**: Self Edge", report)
        self.assertIn("Not computed because the graph contains a cycle", report)

    def test_multi_node_cycle_skips_longest_path_without_false_self_edge(self):
        report = self.generate(
            [
                {
                    "ConceptID": "1",
                    "ConceptLabel": "First",
                    "Dependencies": "2",
                    "TaxonomyID": "TEST",
                },
                {
                    "ConceptID": "2",
                    "ConceptLabel": "Second",
                    "Dependencies": "1",
                    "TaxonomyID": "TEST",
                },
            ]
        )

        self.assertIn("**Valid DAG Structure**: ❌ No", report)
        self.assertIn("**Self-Dependencies**: None detected ✅", report)
        self.assertIn("Not computed because the graph contains a cycle", report)

    def test_valid_dag_still_reports_the_longest_path(self):
        report = self.generate(
            [
                {
                    "ConceptID": "1",
                    "ConceptLabel": "Foundation",
                    "Dependencies": "",
                    "TaxonomyID": "TEST",
                },
                {
                    "ConceptID": "2",
                    "ConceptLabel": "Middle",
                    "Dependencies": "1",
                    "TaxonomyID": "TEST",
                },
                {
                    "ConceptID": "3",
                    "ConceptLabel": "Advanced",
                    "Dependencies": "2",
                    "TaxonomyID": "TEST",
                },
            ]
        )

        self.assertIn("**Valid DAG Structure**: ✅ Yes", report)
        self.assertIn("**Self-Dependencies**: None detected ✅", report)
        self.assertIn("**Maximum Dependency Chain Length**: 3", report)


if __name__ == "__main__":
    unittest.main()
