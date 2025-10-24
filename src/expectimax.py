from game_config import GameConfig, ExpectimaxConfig  # pylint: disable=import-error

class Expectimax: # pylint: disable=too-many-instance-attributes
    """
    The code for the Expectimax algorithm

    Attributes:
        max_depth (int): Maximum depth of the search tree
        tile_count (int): Number of rows and columns
    """

    def __init__(self): # pylint: disable=too-many-instance-attributes
        """
        Initialize the data for the algorithm

        Attributes:
            max_depth (int): Maximum depth of the search tree
            tile_count (int): Number of rows and columns
        """
        self.max_depth = ExpectimaxConfig.MAX_DEPTH
        self.tile_count = GameConfig.TILE_COUNT
        self.cache = {}

        self.snake_0_0 = [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 3), (1, 2), (1, 1), (1, 0),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 3), (3, 2), (3, 1), (3, 0)
        ]
        self.snake_0_3 = [(row, self.tile_count - 1 - column) for row, column in self.snake_0_0]
        self.snake_3_0 = [(self.tile_count - 1 - row, column) for row, column in self.snake_0_0]
        self.snake_3_3 = [(self.tile_count - 1 - row, self.tile_count - 1 - column) for row, column in self.snake_0_0]

    def get_best_move(self, board):
        """
        Called from the index.py, handles the running and returning of the best move. At start clears all caches

        Returns:
            The best move to make based on the current board state as a string "left", "right", "up", "down"
        """
        self.max_depth = ExpectimaxConfig.MAX_DEPTH

        empty = sum(row.count(0) for row in board)

        self.cache.clear()

        if ExpectimaxConfig.CHANGE_DEPTH:
            if empty <= 4:
                self.max_depth = self.max_depth + 1
            elif empty >= 7:
                self.max_depth = self.max_depth - 1

        _, move = self.max(board, 0)

        return move

    def evaluate(self, board): # pylint: disable=too-many-locals
        """
        Evaluates the current board state and returns a score based on the board's state.
        Turns the board into a log2 for evaluation so that the size of the tiles does not affect

        Returns:
            The score of the board state as a float
        """

        log_board = [[tile.bit_length() - 1 if tile > 0 else 0 for tile in row]
                     for row in board]

        largest = max(max(row) for row in board)

        empty_ratio = self.get_empty_ratio(board)
        corner = 1.0 if self.get_corner_bonus(board, largest) else 0.0
        snake = self.get_snake_bonus(board, log_board, largest)
        smoothness, merges = self.smoothness_and_merge(board, log_board)

        w_smoothness = ExpectimaxConfig.SMOOTHNESS_BONUS
        w_empty = ExpectimaxConfig.EMPTY_TILE
        w_corner = ExpectimaxConfig.CORNER_BONUS
        w_snake = ExpectimaxConfig.SNAKE_BONUS
        w_merge = ExpectimaxConfig.MERGE_BONUS

        total_score = (
            empty_ratio * w_empty +
            corner * w_corner +
            merges * w_merge +
            snake * w_snake +
            smoothness * w_smoothness
        )

        return total_score, None

    def get_empty_ratio(self, board):
        """
        Calculate the ratio of empty tiles to filled ones, to get bonus for empty tiles

        Returns:
            The ratio of empty tiles to filled ones as float
        """
        empty_counter = 0
        for row in board:
            for cell in row:
                if cell == 0:
                    empty_counter += 1
        return empty_counter / (self.tile_count) ** 2

    def get_corner_bonus(self, board, largest):
        """Check if the larges tile is in a corner

        Returns:
            A bool, True if the largest tile is in a corner, False otherwise
        """
        corners = [board[0][0], board[0][-1], board[-1][0], board[-1][-1]]
        if largest in corners and largest > 0:
            return True
        return False

    def smoothness_and_merge(self, board, log_board):
        """
        Calculate the smoothness of the board. This means it checks neighboring tiles
        and counts their difference, the smaller the better. Also count same tiles
        next to each other, divide it by the maximum to get a useful number, larger numbers = better

        raw smoothness / pairs

        Returns:
            The smoothness score of the board as a float, inverted value since negative is good in this case
            The ratio of potential merges to the maximum possible merges as a float
        """
        n = self.tile_count
        difference = 0.0
        pairs = 0
        potentials = 0
        for row in range(n):
            for column in range(n):
                # Smoothness logic
                if column + 1 < n:
                    difference += abs(log_board[row][column] - log_board[row][column + 1])
                    pairs += 1
                if row + 1 < n:
                    difference += abs(log_board[row][column] - log_board[row + 1][column])
                    pairs += 1

                # Merge logic
                value = board[row][column]
                if value == 0:
                    continue
                if row + 1 < n and board[row + 1][column] == value:
                    potentials += value.bit_length() - 1  # To get the log2
                if column + 1 < n and board[row][column + 1] == value:
                    potentials += value.bit_length() - 1  # To get the log2

        return - (difference/pairs), potentials / (2 * n * (n - 1))

    def get_snake_bonus(self, board, log_board, largest):
        """
        Check if the board has a snake like structure of decreasing numbers
        leaving from the corner where the largest is
        If largest in top left then something like this:

        | 2048 | 1024 | 512  | 256  |
        |  64  |  8   | 32   | 128  |
        |  0   |  0   |  4   |  0   |
        |  2   |  2   |  8   |  0   |

        Row 1: Here the bonus would be for this row +4
        Row 2: Here the bonus goes till the tile with value 8
        Row 3: No bonus here any more
        Row 4: No bonus here any more

        Return:
            The snake bonus as a float
        """
        n = self.tile_count
        corners = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]
        largest_pos = None
        for row, column in corners:
            if largest == board[row][column]:
                largest_pos = (row, column)
        if largest_pos is None:
            return 0

        snake = getattr(self, f"snake_{largest_pos[0]}_{largest_pos[1]}")

        total = sum(sum(row) for row in log_board)
        score = log_board[snake[0][0]][snake[0][1]]
        earlier = score

        for row, column in snake[1:]:
            value = log_board[row][column]
            if value <= earlier and value != 0:
                score += value
                earlier = value
            else:
                return score / total if total > 0 else 0.0

        return score / total if total > 0 else 0.0


    def max(self, board, current_depth):
        """
        The main loop part. This checks each possible move for each step, "left", "right", "up", "down". If the move
        changes the board it is sent to the chance() function. Also checks if the max_depth is reached, and check if
        the current board state already exists in the cache for quicker processing

        Returns:
            Tuple (best score, best move), where best score is a float and best move string
        """
        # Making a cache so the program does not need to count the same thing every time
        board_key = tuple(val for row in board for val in row)
        cache_key = (0, board_key, current_depth)

        if cache_key in self.cache:
            return self.cache[cache_key]

        if current_depth >= self.max_depth:
            # Stores the result in the cache so it can be accessed easily
            result = self.evaluate(board)
            self.cache[cache_key] = result
            return result

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

        result = (best_score, best_move)
        self.cache[cache_key] = result
        return result

    def chance(self, board, current_depth):
        """
        For each board given to this function from the max() it tests all possible spawn points for new
        tiles and gives it the values 2 and 4 and sends it for evaluation. Also checks if the board was already
        in the cache for speedup. The then calculates the expected value for each possible spawn point with
        the chance for 2 and 4 calculated into it. Based on this the algoritm can then know what move has the best
        chance to give the best results

        Returns:
            Tuple (avarage expected, None) where the average expected is calculated value
        """
        board_key = tuple(val for row in board for val in row)
        cache_key = (1, board_key, current_depth)

        if cache_key in self.cache:
            return self.cache[cache_key]

        empty_cells = []
        for i in range(16):
            if board[i//4][i%4] == 0:
                empty_cells.append((i//4, i%4))

        if not empty_cells:
            if self.max_depth == current_depth:
                result = self.evaluate(board)
            else:
                result = 0
            self.cache[cache_key] = result
            return result

        total_expected = 0

        for row, column in empty_cells:

            board[row][column] = 2
            score2, _ = self.max(board, current_depth)

            board[row][column] = 4
            score4, _ = self.max(board, current_depth)

            board[row][column] = 0

            total_expected += 0.9 * score2 + 0.1 * score4

        avg_expected = total_expected / len(empty_cells)
        result = (avg_expected, None)
        self.cache[cache_key] = result
        return result

    def make_move(self, board, move):
        """
        Simulates a move on the board and returns the new board state.

        Return:
            New board as a list
        """
        if move == "left":
            new_board = self.move_left(board)
            return new_board
        if move == "right":
            new_board = self.move_right(board)
            return new_board
        if move == "up":
            new_board = self.move_up(board)
            return new_board
        if move == "down":
            new_board = self.move_down(board)
            return new_board

    def move_left(self, board):
        """
        Simulates a left move on the board and returns the new board state.

        Return:
            New board as a list
        """
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
        """
        Simulates a right move on the board and returns the new board state.

        Return:
            New board as a list
        """
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
        """
        Simulates an up move on the board and returns the new board state.

        Return:
            New board as a list
        """
        n = self.tile_count
        new_board = [[0] * n for _ in range(n)]

        for column in range(n):
            entire_column = [board[row][column] for row in range(n) if board[row][column] != 0]

            i = 0
            while i < len(entire_column) - 1:
                if entire_column[i] == entire_column[i + 1]:
                    entire_column[i] *= 2
                    entire_column[i + 1] = 0
                    i += 2
                else:
                    i += 1

            new_tiles = [value for value in entire_column if value != 0]
            for row, value in enumerate(new_tiles):
                new_board[row][column] = value

        return new_board

    def move_down(self, board):
        """
        Simulates a down move on the board and returns the new board state.

        Return:
            New board as a list
        """
        n = self.tile_count
        new_board = [[0] * n for _ in range(n)]

        for column in range(n):
            entire_column = [board[row][column] for row in range(n) if board[row][column] != 0]

            i = len(entire_column) - 1
            while i > 0:
                if entire_column[i] == entire_column[i - 1]:
                    entire_column[i] *= 2
                    entire_column[i - 1] = 0
                    i -= 2
                else:
                    i -= 1

            new_tiles = [value for value in entire_column if value != 0]
            for row, value in enumerate(new_tiles):
                new_board[n - len(new_tiles) + row][column] = value

        return new_board
