from game_config import GameConfig

class Expectimax:
    def __init__(self):
        self.max_depth = GameConfig.MAX_DEPTH
        self.tile_count = GameConfig.TILE_COUNT

    def get_best_move(self, board):
        # Called from outside, return "left" "right" "up" "down"
        best_score, best_move = self.max(board, 0)
        print(best_score, best_move)
        if best_move is None:
            return "left"
        return best_move

    def evaluate(self, board):
        pass

    def max(self, board, current_depth):
        # Try all 4 possible moves, return best one



        if current_depth >= self.max_depth:
            return 1, None

        best_score = float('-inf') # Worst possible score
        best_move = None

        for move in ["left", "right", "up", "down"]:
            print("\nCurrent depth: ", current_depth)
            print("Next move: ", move)
            new_board = self.make_move(board, move)

            if new_board == board:
                continue

            score, move = self.max(new_board, current_depth + 1)

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def chance(self, board, current_depth):
        # TYÖN ALLA
        empty_cells = []

        for r in board:
            for c in r:
                if c == 0:
                    empty_cells.append((r, c))

        if not empty_cells:
            return self.evaluate(board), None

        expected_score = 0

        for r,c in empty_cells:
            new_board_2 = [row[:] for row in board]
            new_board_2[r][c] = 2
            score_2 = self.evaluate(new_board_2)





        pass

    def make_move(self, board, move):
        # Implement the logic to simulate a move on the board
        if move == "left":
            print("Board before move left: \n", board[0], "\n", board[1], "\n", board[2], "\n", board[3], "\n")
            new_board = self.move_left(board)
            print("Moving left makes board: \n", new_board[0], "\n", new_board[1], "\n", new_board[2], "\n", new_board[3], "\n")
            return new_board
        elif move == "right":
            print("Board before move right: \n", board[0], "\n", board[1], "\n", board[2], "\n", board[3], "\n")
            new_board = self.move_right(board)
            print("Moving right makes board: \n", new_board[0], "\n", new_board[1], "\n", new_board[2], "\n", new_board[3], "\n")
            return new_board
        elif move == "up":
            print("Board before move up: \n", board[0], "\n", board[1], "\n", board[2], "\n", board[3], "\n")
            new_board = self.move_up(board)
            print("Moving up makes board: \n", new_board[0], "\n", new_board[1], "\n", new_board[2], "\n", new_board[3], "\n")
            return new_board
        elif move == "down":
            print("Board before move down: \n", board[0], "\n", board[1], "\n", board[2], "\n", board[3], "\n")
            new_board = self.move_down(board)
            print("Moving down makes board: \n", new_board[0], "\n", new_board[1], "\n", new_board[2], "\n", new_board[3], "\n")
            return new_board

    def move_left(self, board):
        new_board = []

        for r in board:
            tiles = [value for value in r if value != 0]
            c = 0
            while c < len(tiles) - 1:
                if tiles[c] == tiles[c+1]:
                    tiles[c] *= 2
                    del tiles[c + 1]
                c += 1

            new_row = tiles + [0] * (self.tile_count - len(tiles))
            new_board.append(new_row)

        return new_board

    def move_right(self, board):
        new_board = []

        for r in board:
            tiles = [value for value in r if value != 0]
            c = len(tiles) - 1
            while c > 0:
                if tiles[c] == tiles[c-1]:
                    tiles[c] *= 2
                    del tiles[c - 1]
                c -= 1

            new_row = [0] * (self.tile_count - len(tiles)) + tiles
            new_board.append(new_row)

        return new_board

    def move_up(self, board):
        new_board = [[0] * self.tile_count for _ in range(self.tile_count)]

        for c in range(self.tile_count):
            column = [board[r][c] for r in range(self.tile_count) if board[r][c] != 0]

            i = 0
            while i < len(column) - 1:
                if column[i] == column[i+1]:
                    column[i] *= 2
                    del column[i + 1]
                i += 1

            for r in range(len(column)):
                new_board[r][c] = column[r]

        return new_board

    def move_down(self, board):
        new_board = [[0] * self.tile_count for _ in range(self.tile_count)]

        for c in range(self.tile_count):
            column = [board[r][c] for r in range(self.tile_count) if board[r][c] != 0]

            i = len(column) - 1
            while i > 0:
                if column[i] == column[i - 1]:
                    column[i] *= 2
                    del column[i - 1]
                    i -= 1
                i -= 1

            for i, value in enumerate(column):
                new_board[self.tile_count - i - 1][c] = value

        return new_board
