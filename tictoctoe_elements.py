from prompt_toolkit import prompt
import random, numpy

class tictoctoe_elements:
    def display_game_board(self, board):
        for row in board:
            print("|", row[0], "|", row[1], "|", row[2], "|")

    def players(self):
        human = random.choice("XO")
        if human == "X":
            computer = "O"
        else:
            computer = "X"    
        return {"human":human, "computer":computer}

    def tictoctoe_cursor(self):
        move = prompt("tictoctoe> ")
        if move == "quite":
            return "quite"
        else:
            x = int(move.split(",")[0].split(" ")[1])
            y = int(move.split(",")[1])
            return x, y

    def display_notes(self):
        notes = [
            "1. Just use 'move a,b' to make a move !",
            "2. a and b both from 0 to 2 means 3*3 game board size",
            "3. Type 'quite' to quite the game",
            "4. You quite you lose"
        ]
        return [print(note) for note in notes]