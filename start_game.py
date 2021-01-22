from tictoctoe_elements import tictoctoe_elements


tictoctoe_funcs = tictoctoe_elements()

def human_turn(board):
    move = tictoctoe_funcs.tictoctoe_cursor()
    if move == "quite":
        tictoctoe_funcs.display_game_board(board)
        print("you loosed")
        
    else:
        board[move] = players["human"]

def computer_turn(board):
    empty_positions = numpy.where(board == " ")
    x, y = random.choice(empty_positions[0]), random.choice(empty_positions[1])
    board[x, y] = players["computer"]
    print("computer's move:", "move ", x, y)
    tictoctoe_funcs.display_game_board(board)


def start(board, players, human = False):
    print("human:", human)
    if human == True:
        while True:                
        # human's turn
            human_turn(board)

        # computer's turn
            computer_turn(board)

    else:
        while True:
        # computer's turn
            computer_turn(board)
        # human's turn
            human_turn(board)

