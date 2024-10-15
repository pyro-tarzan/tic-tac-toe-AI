from singleplayer import SinglePlayer
from multiplayer import Multiplayer
from os import system

mp = Multiplayer()
print("Welcome to Tic Tac Toe.")
print("Choose mode:\n\tSingle Player: 0\n\tMutiplayer: 1")

is_valid_mode = False
while not is_valid_mode:

    try:
        player_method = int(input())
        if player_method == 0:
            is_valid_mode = True
            sp = SinglePlayer()

            cpu = None
            player = ""
            while cpu is None:
                player = input("choose x or o: ")
                cpu = sp.cpu_choice(player)

            while True:
                if player == "x":
                    # Start from player
                    sp.print_list()
                    if sp.check_win(sp.updatable_list) == player:
                        print(f"Player Win.")
                        break
                    elif sp.check_win(sp.updatable_list) == cpu:
                        print("CPU Win.")
                        break
                    elif sp.check_for_draw():
                        print("Match Draw.")
                        break
                    sp.move_player(player)
                    sp.print_list()
                    if sp.check_win(sp.updatable_list) == player:
                        print(f"Player Win.")
                        break
                    elif sp.check_win(sp.updatable_list) == cpu:
                        print("CPU Win.")
                        break
                    elif sp.check_for_draw():
                        print("Match Draw.")
                        break
                    sp.move_cpu(cpu, player)

                else:
                    # Start from CPU
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
    except ValueError:
        system("cls")
        print("\"INVALID INPUT\"\nChoose mode:\n\tSingle Player: 0\n\tMutiplayer: 1")
