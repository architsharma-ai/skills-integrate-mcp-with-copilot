import os
import sys
import unittest

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import app as app_module


class ActivityEndpointTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app_module.app)

    def test_github_skills_activity_is_available(self):
        response = self.client.get("/activities")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn("GitHub Skills", body)
        self.assertEqual(
            body["GitHub Skills"]["description"],
            "Learn practical coding and collaboration skills through GitHub workshops and projects"
        )


if __name__ == "__main__":
    unittest.main()
