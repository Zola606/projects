import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class PortfolioTests(unittest.TestCase):
    def test_twenty_projects_have_metadata(self):
        projects = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit())
        self.assertEqual(len(projects), 20)
        categories = [
            json.loads((project / "project.json").read_text())["category"]
            for project in projects
        ]
        self.assertEqual(categories.count("cisco-network-security"), 10)
        self.assertEqual(categories.count("cybersecurity-soc"), 10)
        for project in projects:
            metadata = project / "project.json"
            self.assertTrue(metadata.exists(), project)
            data = json.loads(metadata.read_text())
            self.assertTrue(data["title"])
            self.assertIn(data["category"], {"cisco-network-security", "cybersecurity-soc"})
            self.assertTrue((project / "README.md").exists())

    def test_no_project_contains_live_secrets_or_unsafe_scan_defaults(self):
        for path in ROOT.glob("**/*"):
            if (
                path.is_file()
                and ".git" not in path.parts
                and "__pycache__" not in path.parts
                and path != pathlib.Path(__file__)
            ):
                text = path.read_text(errors="ignore").lower()
                self.assertNotIn("password=", text)
                self.assertNotIn("api_key=", text)
                self.assertNotIn("nmap -p-", text)
                self.assertNotIn("rm -rf /", text)

    def test_ten_packet_tracer_project_packs_have_metadata(self):
        projects = sorted((ROOT / "packet-tracer").glob("*/project.json"))
        self.assertEqual(len(projects), 10)
        for metadata in projects:
            project = metadata.parent
            self.assertTrue((project / "README.md").exists())
            self.assertTrue((project / "topology.txt").exists())


if __name__ == "__main__":
    unittest.main()

