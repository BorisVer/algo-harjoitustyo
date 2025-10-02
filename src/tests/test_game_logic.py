import unittest
from game_config import GameConfig
from game.game_logic import GameLogic, Tile
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game = GameLogic()
        self.config = GameConfig()

    def _set_grid(self, start):
        for row in range(self.config.TILE_COUNT):
            for col in range(self.config.TILE_COUNT):
                value = start[row][col]
                self.game.grid[row][col] = Tile(
                    value, row, col) if value else None

    def test_return_board_returns_correct_board(self):
        start = [
            [0, 0, 0, 0],
            [2, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self._set_grid(start)
        board = self.game.return_board()

        self.assertEqual(board, start)

    def test_no_tile_spaw_at_full_board(self):
        start = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self._set_grid(start)
        spawned_tile = self.game.spawn_tile()
        self.assertIsNone(spawned_tile)

    def test_check_game_is_over_when_no_moves(self):
        start = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]
        self._set_grid(start)
        self.game.move("left")

        self.assertTrue(self.game.game_over)
