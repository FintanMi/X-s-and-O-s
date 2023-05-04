def playing_board(positions):

    board = (f"{positions[1]}|{positions[2]}|{positions[3]}\n"
             f"{positions[4]}|{positions[5]}|{positions[6]}\n"
             f"{positions[7]}|{positions[8]}|{positions[9]}\n")
    print(board)

import random

def who_starts_game():
    
    coin_flip = random.randint(0,1)

    if coin_flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

def win_check(positions):
    if (positions[1] == positions[2] == positions[3]) \
       or (positions[4] == positions[5] == positions[6]) \
        or (positions[7] == positions[8] == positions[9]):
        return True
    elif (positions[1] == positions[4] == positions[7]) \
        or (positions[2] == positions[5] == positions[8]) \
        or (positions[3] == positions[6] == positions[9]):
        return True
    elif (positions[1] == positions[5] == positions[9]) \
        or (positions[3] == positions[5] == positions[7]):
        return True
    else:
        return False