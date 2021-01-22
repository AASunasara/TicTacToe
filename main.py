from tictoctoe_elements import tictoctoe_elements
from start_game import start
import numpy


def main():

    live_board = numpy.array([
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ])

    tictoctoe_funcs = tictoctoe_elements()
    player_details = tictoctoe_funcs.players()
    print(player_details, "\n")

    print("##########  Note:  ##########\n")
    tictoctoe_funcs.display_notes()

    tictoctoe_funcs.display_game_board(live_board)
    if player_details["human"] == "X":
        print("\nYou can start first 'X' is yours !\n")
        print("########## start ##########\n")
        start(live_board, player_details, True)
    else:
        print("\nI will start first 'X' is mine !", "You are biggg 'O' ;)\n")
        print("########## start ##########\n")
        start(live_board, player_details)
        

if __name__ == "__main__":
    main()