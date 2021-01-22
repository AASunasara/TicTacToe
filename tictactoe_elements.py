from prompt_toolkit import prompt
import random, numpy

class tictactoe_elements:
    game_board = numpy.array([
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ])
    score_board = {
        "user" : 0,
        "computer" : 0,
        "draws" : 0
    }
    def display_game_board(self, board):
        for row in board:
            print("|", row[0], "|", row[1], "|", row[2], "|")

    def display_score_board(self, score_board):
        print("|Computer |User |Draws |")
        print("|{}        |{}    |{}     |".format(score_board["computer"], score_board["user"], score_board["draws"]))

    def players(self):
        human = random.choice("XO")
        if human == "X":
            computer = "O"
        else:
            computer = "X"    
        return {"human":human, "computer":computer}

    def display_notes(self):
        notes = [
            "1. Just use 'move a,b' to make a move !",
            "2. a and b both from 0 to 2 means 3*3 game board size.",
            "3. Type 'quit' to quit the game and 'scoreboard' to check history.",
            "4. You quit you lose.",
        ]
        return [print(note) for note in notes]

    def check_for_wins(self, game_board, x, y):
        # check verical and horizontal lines
        if game_board[0][y] == game_board[1][y] == game_board[2][y]:
            return True
        elif game_board[x][0] == game_board[x][1] == game_board[x][2]:
            return True
        # check both diagonals 
        elif x == y and game_board[0][0] == game_board[1][1] == game_board[2][2]:
            return True
        elif x + y == 2 and game_board[0][2] == game_board[1][1] == game_board[2][0]:
            return True
        else:
            # no wins
            return False