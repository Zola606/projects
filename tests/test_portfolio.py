import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class PortfolioTests(unittest.TestCase):
    def test_ten_projects_have_metadata(self):
        projects = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit())
        self.assertEqual(len(projects), 10)
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


if __name__ == "__main__":
    unittest.main()

