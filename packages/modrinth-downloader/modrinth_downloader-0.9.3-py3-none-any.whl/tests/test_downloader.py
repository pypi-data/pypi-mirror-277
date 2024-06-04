import unittest
from modrinth_downloader.downloader import download_project

class TestDownloader(unittest.TestCase):

    def test_download_project(self):
        project_id = "example_project_id"
        result = download_project(project_id)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
