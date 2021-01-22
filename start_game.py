from tictactoe_elements import tictactoe_elements
import numpy, random
from prompt_toolkit import prompt

tictactoe_funcs = tictactoe_elements()
game_board = numpy.array([
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
])

def human_turn():
    """
    this function will handle the input form human player.
    """
    while True:
        try:
            move = prompt("tictactoe> ")
            if move == "quit":
                tictactoe_funcs.display_game_board(game_board)
                print("you loosed....")
                return "quit"
            else:
                x = int(move.split(",")[0].split(" ")[1])
                y = int(move.split(",")[1])

                if game_board[x,y] == " ":
                    game_board[x, y] = players_details["human"]
                    tictactoe_funcs.display_game_board(game_board)
                    return
                else:
                    print("Invalid move, Place already taken.")
        except:
            print("Try again!")
            tictactoe_funcs.display_notes()
            continue

def computer_turn():
    """
    This function will make a move randomly and 
    make sure the place is already not taken.
    """
    empty_positions = numpy.where(game_board == " ")
    if len(empty_positions[0]) > 0:
        move = random.randrange(len(empty_positions[0]))
        x, y = empty_positions[0][move], empty_positions[1][move]
        game_board[x, y] = players_details["computer"]
        print("Computer> :", ("move {},{}".format(x, y)))
        tictactoe_funcs.display_game_board(game_board)
    else:
        # There is no any empty place
        return "quit"

def start(players, human = False):
    global players_details 
    players_details = players
    if human == True:
        # If the human got 'X' sign.
        while True:                
            move = human_turn()
            if move == "quit":
                break
            move = computer_turn()
            if move == "quit":
                break    
    else:
        # If computer got 'X' sign.
        while True:
            move = computer_turn()
            if move == "quit":
                break
            move = human_turn()
            if move == "quit":
                break