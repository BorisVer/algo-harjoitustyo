from game_config import GameConfig, ExpectimaxConfig

class Expectimax:
    def __init__(self):
        self.max_depth = ExpectimaxConfig.MAX_DEPTH
        self.tile_count = GameConfig.TILE_COUNT

    def get_best_move(self, board):
        # Called from outside, return "left" "right" "up" "down"
        best_score, best_move = self.max(board, 0)

        self.evaluate_with_print(board)

        return best_move

    def evaluate_with_print(self, board):
        empty_counter = 0
        tiles = []
        for row in board:
            for cell in row:
                tiles.append(cell)
                if cell == 0:
                    empty_counter += 1
        empty_ratio = empty_counter / (self.tile_count ** 2)

        corner = 1.0 if self.get_corner_bonus(board) else 0.0

        snake = self.get_snake_bonus(board)

        adjacent = self.get_adjacent_bonus(board)

        big_center = self.check_big_center(board)

        w_empty = ExpectimaxConfig.EMPTY_TILE
        w_corner = ExpectimaxConfig.CORNER_BONUS
        w_adjacent = ExpectimaxConfig.ADJACENT_BONUS
        w_snake = ExpectimaxConfig.SNAKE_BONUS
        w_center = ExpectimaxConfig.CENTER_PENALTY

        print("Current board:")
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
        print("Points from empty tiles:", empty_ratio * w_empty)
        print("Points from corner tiles:", corner * w_corner)
        print("Points from adjacent tiles:", adjacent * w_adjacent)
        print("Points from snake tiles:", snake * w_snake)
        print("Penalty from big center:", big_center * w_center)

        total_score = (
                    empty_ratio * w_empty +
                    corner * w_corner +
                    adjacent * w_adjacent +
                    snake * w_snake +
                    big_center * w_center
                )

        print("Total score:", total_score)

        return total_score, None

    def evaluate(self, board):
        empty_counter = 0
        tiles = []
        for row in board:
            for cell in row:
                tiles.append(cell)
                if cell == 0:
                    empty_counter += 1
        empty_ratio = empty_counter / (self.tile_count ** 2)

        corner = 1.0 if self.get_corner_bonus(board) else 0.0

        snake = self.get_snake_bonus(board)

        adjacent = self.get_adjacent_bonus(board)

        big_center = self.check_big_center(board)

        w_empty = ExpectimaxConfig.EMPTY_TILE
        w_corner = ExpectimaxConfig.CORNER_BONUS
        w_adjacent = ExpectimaxConfig.ADJACENT_BONUS
        w_snake = ExpectimaxConfig.SNAKE_BONUS
        w_center = ExpectimaxConfig.CENTER_PENALTY

        total_score = (
                    empty_ratio * w_empty +
                    corner * w_corner +
                    adjacent * w_adjacent +
                    snake * w_snake +
                    big_center * w_center
                )

        return total_score, None

    def get_corner_bonus(self, board):
        largest = max(max(row) for row in board)
        corners = [board[0][0]] #[board[0][0], board[0][-1], board[-1][0], board[-1][-1]]
        for corner in corners:
            if corner == largest and largest > 0:
                return True
        return False

    def get_snake_bonus(self, board):
        total_sum = sum(sum(row) for row in board)
        score = board[0][0]
        earlier = board[0][0]
        order = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0)]
        for r, c in order:
            if board[r][c] <= earlier and board[r][c] != 0:
                score += board[r][c]
                earlier = board[r][c]
            else:
                return score / total_sum

        return score / total_sum

    def get_adjacent_bonus(self, board):
        score = 0.0
        n = self.tile_count
        larges = max(max(row) for row in board)

        for r in range(n - 1):
            for c in range(n - 1):
                value = board[r][c]
                if value == 0:
                    continue

                if board[r + 1][c] == value and r + 1 < n:
                    if board[r + 1][c] == larges:
                        score += 2
                    score += 1
                elif board[r + 1][c] == value / 2 or board[r + 1][c] == value * 2:
                    if board[r + 1][c] == larges:
                        score += 1.5
                    score += 0.75

                if board[r][c + 1] == value and c + 1 < n:
                    if board[r][c + 1] == larges:
                        score += 2
                    score += 1

                elif board[r][c + 1] == value / 2 or board[r][c + 1] == value * 2:
                    if board[r][c + 1] == larges:
                        score += 1.5
                    score +=  0.75

        return score

    def check_big_center(self, board):
        check = [(1,1), (1,2), (2,1), (2,2)]
        largest = max(max(row) for row in board)
        counter = 0
        for r, c in check:
            if board[r][c] == largest or board[r][c] == largest / 2:
                counter -= 1
        return counter

    def max(self, board, current_depth):
        if current_depth >= self.max_depth:
            return self.evaluate(board)

        best_score = float('-inf')
        best_move = None
        valid_moves = []

        for move in ["left", "right", "up", "down"]:
            new_board = self.make_move(board, move)

            if new_board == board:
                continue

            score, _ = self.chance(new_board, current_depth + 1)
            valid_moves.append((move, score))

            if score > best_score:
                best_score = score
                best_move = move

        if best_move is None and valid_moves:
            valid_moves.sort(key=lambda x: x[1], reverse=True)
            best_move = valid_moves[0][0]
            best_score = valid_moves[0][1]

        if best_move is None:
            return self.evaluate(board)

        return best_score, best_move

    def chance(self, board, current_depth):
        empty_cells = []

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    empty_cells.append((r, c))

        if not empty_cells:
            return self.evaluate(board)

        total_expected_score = 0

        for r, c in empty_cells:
            new_board_2 = [row[:] for row in board]
            new_board_2[r][c] = 2
            score_2, _ = self.max(new_board_2, current_depth + 1)

            new_board_4 = [row[:] for row in board]
            new_board_4[r][c] = 4
            score_4, _ = self.max(new_board_4, current_depth + 1)

            expected_score = 0.9 * score_2 + 0.1 * score_4
            total_expected_score += expected_score

        average_expected_score = total_expected_score / len(empty_cells)

        return average_expected_score , None

    def make_move(self, board, move):
        # Implement the logic to simulate a move on the board
        if move == "left":
            new_board = self.move_left(board)
            return new_board
        elif move == "right":
            new_board = self.move_right(board)
            return new_board
        elif move == "up":
            new_board = self.move_up(board)
            return new_board
        elif move == "down":
            new_board = self.move_down(board)
            return new_board

    def move_left(self, board):
        new_board = []
        for row in board:
            tiles = [v for v in row if v != 0]

            i = 0
            while i < len(tiles) - 1:
                if tiles[i] == tiles[i + 1]:
                    tiles[i] *= 2
                    tiles[i + 1] = 0
                    i += 2
                else:
                    i += 1

            new_tiles = [v for v in tiles if v != 0]
            new_row = new_tiles + [0] * (self.tile_count - len(new_tiles))
            new_board.append(new_row)

        return new_board

    def move_right(self, board):
        new_board = []
        for row in board:
            tiles = [v for v in row if v != 0]

            i = len(tiles) - 1
            while i > 0:
                if tiles[i] == tiles[i - 1]:
                    tiles[i] *= 2
                    tiles[i - 1] = 0
                    i -= 2
                else:
                    i -= 1

            new_tiles = [v for v in tiles if v != 0]
            new_row = [0] * (self.tile_count - len(new_tiles)) + new_tiles
            new_board.append(new_row)

        return new_board

    def move_up(self, board):
        n = self.tile_count
        new_board = [[0] * n for _ in range(n)]

        for c in range(n):
            column = [board[r][c] for r in range(n) if board[r][c] != 0]

            i = 0
            while i < len(column) - 1:
                if column[i] == column[i + 1]:
                    column[i] *= 2
                    column[i + 1] = 0
                    i += 2
                else:
                    i += 1

            new_tiles = [v for v in column if v != 0]
            for r, v in enumerate(new_tiles):
                new_board[r][c] = v

        return new_board

    def move_down(self, board):
        n = self.tile_count
        new_board = [[0] * n for _ in range(n)]

        for c in range(n):
            column = [board[r][c] for r in range(n) if board[r][c] != 0]

            i = len(column) - 1
            while i > 0:
                if column[i] == column[i - 1]:
                    column[i] *= 2
                    column[i - 1] = 0
                    i -= 2
                else:
                    i -= 1

            new_tiles = [v for v in column if v != 0]
            for i, v in enumerate(new_tiles):
                new_board[n - len(new_tiles) + i][c] = v

        return new_board
