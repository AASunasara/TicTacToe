from tictactoe_elements import tictactoe_elements
from start_game import start
import numpy


def main():
    tictactoe_funcs = tictactoe_elements()
    player_details = tictactoe_funcs.players()
    
    print("##########  :Note:  ##########\n")
    tictactoe_funcs.display_notes()

    if player_details["human"] == "X":
        print("\nYou will start first, 'X' is yours !")
        start(player_details, True)
    else:
        print("\nI will start first, 'X' is mine !", "You are biggg 'O' ;)")
        start(player_details)
        

if __name__ == "__main__":
    main()