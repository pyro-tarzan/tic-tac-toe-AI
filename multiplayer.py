from tictactoe import TicTacToe

class Multiplayer (TicTacToe):
    def player_turn(self, x_or_o, name):
        choice = ""
        if x_or_o == "x":
            choice = input(f"{name}: ")
        elif x_or_o == "o":
            choice = input(f"{name}: ")
        if 10 > int(choice) > 0:
            # Player can proceed
            for row_index in range(0, len(self.updatable_list)):
                for column_index in range(0, len(self.updatable_list[row_index])):
                    if self.updatable_list[row_index][column_index] == choice:
                        self.updatable_list[row_index][column_index] = x_or_o
                        self.count += 1
                        return self.updatable_list
            if self.count == 9:
                print("Nothing to add.")
            else:
                print("Already Exist.")
                return self.player_turn(x_or_o, name)

        else:
            # Player1 can't proceed
            print("Invalid input.")
            return self.player_turn(x_or_o, name)
