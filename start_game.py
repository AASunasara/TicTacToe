from tictactoe_elements import tictactoe_elements
import numpy, random
from prompt_toolkit import prompt

tictactoe_funcs = tictactoe_elements()
game_board = tictactoe_funcs.game_board
score_board = tictactoe_funcs.score_board


def clean_game_board():
    for row in game_board:
        row[0], row[1], row[2] = " ", " ", " "

def human_turn():
    """
    this function will handle the input form human player.
    """
    while True:
        try:
            move = prompt("\ntictactoe> ")
            if move == "quit":
                tictactoe_funcs.display_game_board(game_board)
                print("Computer wins!")
                return "game end"
            elif move == "scoreboard":
                tictactoe_funcs.display_score_board(score_board)
            else:
                x = int(move.split(",")[0].split(" ")[1])
                y = int(move.split(",")[1])
                if game_board[x,y] == " ":
                    game_board[x, y] = players_details["human"]
                    # check if wins
                    wins = tictactoe_funcs.check_for_wins(game_board, x, y)
                    if wins == True:
                        score_board["user"] += 1
                        tictactoe_funcs.display_game_board(game_board)
                        print("User wins!\n", "Game Reseted.")
                        return "restart"
                    tictactoe_funcs.display_game_board(game_board)
                    break
                else:
                    if len(numpy.where(game_board == " ")) == 0:
                        score_board["draws"] += 1
                        print("The game is a Draw")
                        return "game end"
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
        # will take random move
        move = random.randrange(len(empty_positions[0]))
        x, y = empty_positions[0][move], empty_positions[1][move]
        game_board[x, y] = players_details["computer"]
        # check if wins
        wins = tictactoe_funcs.check_for_wins(game_board, x, y)
        if wins == True:
            score_board["computer"] += 1
            print("\nComputer :", ("move {},{}".format(x, y)))
            tictactoe_funcs.display_game_board(game_board)
            print("Computer wins!\n", "Game Reseted.")
            return "restart"
        else:
           print("\nComputer :", ("move {},{}".format(x, y)))
           tictactoe_funcs.display_game_board(game_board)
    else:
        # There is no any empty place available
        score_board["draws"] += 1
        print("The game is a Draw")
        return "game end"

def start(players, human = False):
    global players_details 
    players_details = players
    if human == True:
        # If the human got 'X' sign.
        while True:                
            response = human_turn()
            if response == "game end":
                break
            elif response == "restart":
                clean_game_board()
                
            response = computer_turn()
            if response == "game end":
                break
            elif response == "restart":
                clean_game_board()
                
    else:
        # If computer got 'X' sign.
        while True:
            response = computer_turn()
            if response == "game end":
                break
            elif response == "restart":
                clean_game_board()
                
            response = human_turn()
            if response == "game end":
                break
            elif response == "restart":
                clean_game_board()
                