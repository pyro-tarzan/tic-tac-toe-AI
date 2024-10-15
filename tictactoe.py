class TicTacToe:
    def __init__(self):
        self.updatable_list = [["1", "2", "3"],
                               ["4", "5", "6"],
                               ["7", "8", "9"]]

        self.is_game_over = False
        self.count = 0

    def check_win(self, name):
        for row_index in range(0, 3):
            if (self.updatable_list[row_index][0] == self.updatable_list[row_index][1] and
                    self.updatable_list[row_index][1] == self.updatable_list[row_index][2]):
                self.is_game_over = True
                print(f"{name} Won")
                return True

        for col_index in range(0, 3):
            if (self.updatable_list[0][col_index] == self.updatable_list[1][col_index] and
                    self.updatable_list[1][col_index] == self.updatable_list[2][col_index]):
                self.is_game_over = True
                print(f"{name} Won")
                return True

        if (self.updatable_list[0][0] == self.updatable_list[1][1] and
                self.updatable_list[1][1] == self.updatable_list[2][2]):
            self.is_game_over = True
            print(f"{name} Won")
            return True

        if (self.updatable_list[0][2] == self.updatable_list[1][1] and
                self.updatable_list[1][1] == self.updatable_list[2][0]):
            self.is_game_over = True
            print(f"{name} Won")
            return True

        if self.count == 9:
            print("Match Draw.")
            self.is_game_over = True
            return True

    def print_list(self):
        for row_index in range(0, 3):
            row_list = ""
            for column_index in range(0, 3):
                row_list += f" {self.updatable_list[row_index][column_index]} "
            print(row_list)
