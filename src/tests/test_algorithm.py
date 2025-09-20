from src.expectimax import Expectimax
import unittest

class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        self.expectimax = Expectimax()

    def test_move_left_simple(self):
        board = [
            [0, 0, 2, 0,],
            [0, 0, 0, 2,],
            [0, 0, 0, 0,],
            [0, 2, 0, 0,]
        ]

        expected_board = [
            [2, 0, 0, 0,],
            [2, 0, 0, 0,],
            [0, 0, 0, 0,],
            [2, 0, 0, 0,]
        ]
        new_board = self.expectimax.move_left(board)

        self.assertEqual(expected_board, new_board)

    def test_move_right_simple(self):
        board = [
            [0, 0, 2, 0,],
            [0, 0, 0, 2,],
            [0, 0, 0, 0,],
            [0, 2, 0, 0,]
        ]

        expected_board = [
            [0, 0, 0, 2,],
            [0, 0, 0, 2,],
            [0, 0, 0, 0,],
            [0, 0, 0, 2,]
        ]
        new_board = self.expectimax.move_right(board)

        self.assertEqual(expected_board, new_board)

    def test_move_down_simple(self):
        board = [
            [0, 0, 2, 0,],
            [0, 0, 0, 2,],
            [0, 0, 0, 0,],
            [0, 2, 0, 0,]
        ]

        expected_board = [
            [0, 0, 0, 0,],
            [0, 0, 0, 0,],
            [0, 0, 0, 0,],
            [0, 2, 2, 2,]
        ]
        new_board = self.expectimax.move_down(board)

        self.assertEqual(expected_board, new_board)

    def test_move_up_simple(self):
        board = [
            [0, 0, 2, 0,],
            [0, 0, 0, 2,],
            [0, 0, 0, 0,],
            [0, 2, 0, 0,]
        ]

        expected_board = [
            [0, 2, 2, 2,],
            [0, 0, 0, 0,],
            [0, 0, 0, 0,],
            [0, 0, 0, 0,]
        ]
        new_board = self.expectimax.move_up(board)

        self.assertEqual(expected_board, new_board)

    def test_move_left_complex(self):
        board = [
            [512, 512, 2, 2,],
            [128, 512, 2, 2,],
            [4, 4, 2, 4,],
            [2, 2, 2, 2,]
        ]

        expected_board = [
            [1024, 4, 0, 0,],
            [128, 512, 4, 0,],
            [8, 2, 4, 0,],
            [4, 4, 0, 0,]
        ]

        new_board = self.expectimax.move_left(board)

        self.assertEqual(expected_board, new_board)

    def test_move_right_complex(self):
        board = [
            [512, 512, 2, 2,],
            [128, 512, 2, 2,],
            [4, 4, 2, 4,],
            [2, 2, 2, 2,]
        ]

        expected_board = [
            [0, 0, 1024, 4,],
            [0, 128, 512, 4,],
            [0, 8, 2, 4,],
            [0, 0, 4, 4,]
        ]

        new_board = self.expectimax.move_right(board)

        self.assertEqual(expected_board, new_board)

    def test_move_down_complex(self):
        board = [
            [512, 512, 2, 2,],
            [128, 512, 2, 2,],
            [4, 4, 2, 4,],
            [2, 2, 2, 2,]
        ]

        expected_board = [
            [512, 0, 0, 0,],
            [128, 1024, 0, 4,],
            [4, 4, 4, 4,],
            [2, 2, 4, 2,]
        ]

        new_board = self.expectimax.move_down(board)

        self.assertEqual(expected_board, new_board)

    def test_move_up_complex(self):
        board = [
            [512, 512, 2, 2,],
            [128, 512, 2, 2,],
            [4, 4, 2, 4,],
            [2, 2, 2, 2,]
        ]

        expected_board = [
            [512, 1024, 4, 4,],
            [128, 4, 4, 4,],
            [4, 2, 0, 2,],
            [2, 0, 0, 0,]
        ]

        new_board = self.expectimax.move_up(board)

        self.assertEqual(expected_board, new_board)

    def test_empty_when_empty(self):
        board = [
            [0, 0, 0, 0,],
            [0, 0, 0, 0,],
            [0, 0, 0, 0,],
            [0, 0, 0, 0,]
        ]

        empty_value = self.expectimax.get_empty_ratio(board)

        self.assertEqual(empty_value, 1)

    def test_empty_when_full(self):
        board = [
            [2, 2, 2, 2,],
            [2, 2, 2, 2,],
            [2, 2, 2, 2,],
            [2, 2, 2, 2,]
        ]

        empty_value = self.expectimax.get_empty_ratio(board)

        self.assertEqual(empty_value, 0)

    def test_empty_when_complex(self):
        board = [
            [0, 0, 1024, 4,],
            [0, 128, 512, 4,],
            [0, 8, 2, 4,],
            [0, 0, 4, 4,]
        ]

        empty_value = self.expectimax.get_empty_ratio(board)

        expected_value = 6 / 4**2

        self.assertEqual(empty_value, expected_value)

    def test_corner_bonus_one_corner(self):
        board = [
            [512, 128, 2, 2,],
            [128, 256, 2, 2,],
            [4, 4, 2, 4,],
            [2, 2, 2, 2,]
        ]
        largest = 512

        corner_bonus = self.expectimax.get_corner_bonus(board, largest)

        self.assertTrue(corner_bonus)

    def test_corner_bonus_multiple_corner(self):
        board = [
            [512, 128, 2, 512,],
            [128, 256, 2, 2,],
            [4, 4, 2, 4,],
            [512, 2, 2, 2,]
        ]
        largest = 512

        corner_bonus = self.expectimax.get_corner_bonus(board, largest)

        self.assertTrue(corner_bonus)

    def test_corner_bonus_not_in_corner(self):
        board = [
            [512, 128, 2, 512,],
            [128, 1024, 2, 2,],
            [4, 4, 2, 4,],
            [512, 2, 2, 2,]
        ]
        largest = 1024

        corner_bonus = self.expectimax.get_corner_bonus(board, largest)

        self.assertFalse(corner_bonus)

    def test_smoothness_and_merge_complex(self):
        board = [
            [512, 1024, 4, 4,],
            [128, 4, 4, 4,],
            [4, 2, 0, 2,],
            [2, 0, 0, 0,]
        ]
        log_board = [[tile.bit_length() - 1 if tile > 0 else 0 for tile in row]
            for row in board]

        smoothness, merge = self.expectimax.smoothness_and_merge(board, log_board)
        self.assertEqual(smoothness, -1.6666666666666667)
        self.assertEqual(merge, 0.4166666666666667)

    def test_snake_bonus_none(self):
        board = [
            [512, 1024, 4, 4,],
            [128, 4, 4, 4,],
            [4, 2, 0, 2,],
            [2, 0, 0, 0,]
        ]
        largest = 1024
        log_board = [[tile.bit_length() - 1 if tile > 0 else 0 for tile in row]
            for row in board]

        snake = self.expectimax.get_snake_bonus(board, log_board, largest)
        self.assertEqual(snake, 0)

    def test_snake_bonus_large(self):
        board = [
            [1024, 512, 256, 128,],
            [8, 16, 32, 64,],
            [4, 2, 0, 2,],
            [2, 0, 0, 0,]
        ]
        largest = 1024
        log_board = [[tile.bit_length() - 1 if tile > 0 else 0 for tile in row]
            for row in board]
        total = sum(sum(row) for row in log_board)

        snake = self.expectimax.get_snake_bonus(board, log_board, largest)
        self.assertEqual(snake, 55 / total)
