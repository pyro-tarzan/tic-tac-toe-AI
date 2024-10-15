from singleplayer import SinglePlayer
from multiplayer import Multiplayer
from os import system

print("Welcome to Tic Tac Toe.")
print("Choose mode:\n\tSingle Player: 0\n\tMutiplayer: 1")
mp = Multiplayer()

is_valid_mode = False
while not is_valid_mode:
    player_method = int(input())
    if player_method == 0:
        is_valid_mode = True
        sp = SinglePlayer()

        cpu = None
        player = ""
        while cpu is None:
            player = input("choose x or o: ")
            cpu = sp.cpu_choice(player)

        while not sp.is_game_over:
            if player == "x":
                # Start from player
                sp.print_list()
                sp.move_player(player)
                sp.print_list()
                sp.move_cpu(cpu, player)

            else:
                # Start from CPU
                # sp.move_cpu(cpu, player)
                pass

    elif player_method == 1:
        is_valid_mode = True
        mp = Multiplayer()

        while not mp.is_game_over:
            system("cls")
            mp.print_list()
            if mp.check_win("Player_2"):
                break

            player_1 = mp.player_turn("x", "Player_1")

            system("cls")
            mp.print_list()
            if mp.check_win("Player_1"):
                break

            player_2 = mp.player_turn("o", "Player_2")
    else:
        print(f"Please a enter a valid mode.")
