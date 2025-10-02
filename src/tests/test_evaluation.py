from src.expectimax import Expectimax
import unittest
from unittest.mock import patch

class TestEvaluation(unittest.TestCase):

    def setUp(self):
        self.expectimax = Expectimax()

    @patch("src.expectimax.ExpectimaxConfig.EMPTY_TILE", 16.0)
    @patch("src.expectimax.ExpectimaxConfig.CORNER_BONUS", 3.0)
    @patch("src.expectimax.ExpectimaxConfig.SMOOTHNESS_BONUS", 5.0)
    @patch("src.expectimax.ExpectimaxConfig.SNAKE_BONUS", 4.0)
    @patch("src.expectimax.ExpectimaxConfig.MERGE_BONUS", 5.5)
    @patch("src.expectimax.ExpectimaxConfig.CHANGE_DEPTH", True)

    def test_evaluation_for_simple_board(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

        value, _ = self.expectimax.evaluate(board)

        self.assertEqual(value, 16)

    def test_evaluation_for_normal_board(self):
        board = [
            [32, 16, 8, 0],
            [0, 0, 0, 0],
            [6, 0, 2, 0],
            [6, 0, 2, 0]
        ]

        value, _ = self.expectimax.evaluate(board)

        empty = 9 / 4**2 * 16.0
        corner = 3.0
        smoothness = -1.1666666666666667 * 5.0
        snake = 0.6666666666666666 * 4.0
        merge = 0.125 * 5.5
        expected_value = empty + corner + smoothness + snake + merge

        self.assertEqual(value, expected_value)

    def test_for_correct_best_move_1(self):
        board = [
            [32, 0, 8, 0],
            [32, 16, 0, 0],
            [6, 0, 2, 0],
            [6, 0, 2, 0]
        ]

        move = self.expectimax.get_best_move(board)
        self.assertEqual(move, "up")

    def test_for_correct_best_move_2(self):
        board = [
            [0, 0, 8, 0],
            [32, 16, 0, 0],
            [6, 0, 2, 256],
            [6, 256, 512, 0]
        ]

        move = self.expectimax.get_best_move(board)
        self.assertEqual(move, "right")

    def test_for_correct_best_move_3(self):
        board = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [512, 1024, 2048, 4096],
            [0, 0, 0, 0]
        ]
        move = self.expectimax.get_best_move(board)
        self.assertEqual(move, "down")

    def test_for_correct_best_move_4(self):
        board = [
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [4, 4, 0, 0],
            [8, 8, 0, 0]
        ]
        move = self.expectimax.get_best_move(board)
        self.assertEqual(move, "left")

    def test_for_correct_best_move_5(self):
        board = [
            [0, 0, 0, 0],
            [0, 0, 0, 4],
            [4, 2, 2, 0],
            [0, 4, 0, 4]
        ]
        move = self.expectimax.get_best_move(board)
        self.assertEqual(move, "right")
