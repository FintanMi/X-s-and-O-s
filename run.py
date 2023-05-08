from func import playing_board, who_starts_game, check_turn, win_check
import os, random

def main():
    positions = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    play_game = True
    game_finished = False
    turn = 0
    previous_turn = -1
    firstGo = True

    while play_game:
        # Resets the screen to show one board
        os.system('cls' if os.name == 'nt' else 'clear')
        
        playing_board(positions)
        
        # shows which player starts the game
        if (firstGo):
            goes_first = who_starts_game()
            print(goes_first + ' will start the game')
            firstGo = False

        print("Player " + str((turn % 2) + 1) + "'s turn: Pick a position")

        # let player know if turn is invalid
        if previous_turn == turn:
            print('Invalid selection, please pick again')
        previous_turn = turn

        # Get input from player
        choice = input('\n')

        if choice == 'q':
            play_game = False
        # check if input is a number from 1-9
        elif str.isdigit(choice) and int(choice) in positions:
            # check if position has already been taken
            if not positions[int(choice)] in {'X', 'O'}:
                # update the board
                turn += 1
                positions[int(choice)] = check_turn(turn)
            
            # check if someone won
            if win_check(positions):
                play_game, game_finished = False, True
            if turn > 8:
                play_game = False

    # print out the results & draw the board again
    os.system('cls' if os.name == 'nt' else 'clear')
    playing_board(positions)

    if game_finished:
        if check_turn(turn) == 'X':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    else:
        print('Tie game')

    print('Thanks for playing!')
    replay = input('Would you like to play again? y or n?\n')

    if (replay == 'y'):
        main()
    else:
        print('Thanks for playing, goodbye!')

main()   