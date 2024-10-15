class SinglePlayer:

    def __init__(self):
        self.updatable_list = [["_", "_", "_"],
                               ["_", "_", "_"],
                               ["_", "_", "_"]]

        self.placeholder = [[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]

        self.is_game_over = False

    def check_win(self, board):
        for row_index in range(0, 3):
            if (board[row_index][0] == board[row_index][1] and
                    board[row_index][1] == board[row_index][2]):

                return board[row_index][0]

        for col_index in range(0, 3):
            if (board[0][col_index] == board[1][col_index] and
                    board[1][col_index] == board[2][col_index]):

                return board[0][col_index]

        if (board[0][0] == board[1][1] and
                board[1][1] == board[2][2]):

            return board[0][0]

        if (board[0][2] == board[1][1] and
                board[1][1] == board[2][0]):

            return board[0][2]

    def print_list(self):
        for row_index in range(0, 3):
            row_list = ""
            for column_index in range(0, 3):
                row_list += f" {self.updatable_list[row_index][column_index]} "
            print(row_list)

    def cpu_choice(self, player):
        if player == "x":
            return "o"
        elif player == "o":
            return "x"
        else:
            return None

    def move_player(self, player):
        player_turn = int(input("Player: "))

        for row in range(0, len(self.placeholder)):
            for col in range(0, len(self.placeholder[row])):
                if player_turn == self.placeholder[row][col]:
                    self.updatable_list[row][col] = player


    def move_cpu(self, cpu, player):
        row, col = self.best_move(self.updatable_list, player, cpu)
        print(row, col)
        self.updatable_list[row][col] = cpu

    def minmax(self,board , depth, is_maximizing, player, cpu):
        winner = self.check_win(board)
        if winner == "x":
            return 10
        elif winner == "o":
            return -10
        elif all(cell != "_" for row in board for cell in row):
            return 0

        if is_maximizing:
            best_score = -1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "_":
                        board[i][j] = player  # X's turn
                        score = self.minmax(board, depth + 1, False, player, cpu)
                        board[i][j] = "_"
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "_":
                        board[i][j] = cpu  # O's turn
                        score = self.minmax(board, depth + 1, True, player, cpu)
                        board[i][j] = "_"
                        best_score = min(score, best_score)
            return best_score

    def best_move(self, board, player, cpu):
        best_score = -1000
        move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = player  # Assume X is the player
                    score = self.minmax(board, 0, False, player, cpu)
                    board[i][j] = "_"
                    if score > best_score:
                        best_score = score
                        move = (i, j)

        return move