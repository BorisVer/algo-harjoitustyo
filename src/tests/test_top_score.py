import unittest
from game.top_score import TopScore
import tempfile
import os

class TestTopScore(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        self.top_score = TopScore()


    def test_file_is_created_if_not_exist(self):
        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.data_dir))


    def test_if_file_exists_no_error_occures(self):
        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.data_dir))

        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.data_dir))


    def test_top_score_file_initialized_correctly(self):
        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.top_score_file))

        with open(self.top_score.top_score_file, "r") as f:
            content = int(f.read())

        self.assertEqual(content, 0)


    def test_top_score_save_function(self):
        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.top_score_file))

        self.top_score.save_top_score(1820)

        with open(self.top_score.top_score_file, "r") as f:
            content = int(f.read())

        self.assertEqual(content, 1820)


    def test_load_top_score_function(self):
        self.top_score.file_exists()
        self.assertTrue(os.path.exists(self.top_score.top_score_file))

        with open(self.top_score.top_score_file, "w") as f:
            f.write(str(250))

        content = self.top_score.load_top_score()

        self.assertEqual(content, 250)
