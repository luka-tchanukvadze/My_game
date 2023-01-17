import random


def display_board(board):
    print("\n" * 100)
    print('|_' + board[7] + '_|_' + board[8] + '_|_' + board[9] + '_|')
    print('__ __ __ __ __')
    print('|_' + board[4] + '_|_' + board[5] + '_|_' + board[6] + '_|')
    print('__ __ __ __ __')
    print('|_' + board[1] + '_|_' + board[2] + '_|_' + board[3] + '_|')


# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


def player_input():
    markers = ["X", "O"]
    while True:
        marker = (random.choice(markers)).upper()

        if marker == "X":
            return ['X', "O"]
        elif marker == "O":
            return ['O', 'X']

# player_input()


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, '$', 8)
# display_board(test_board)


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3 == mark]) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# print(win_check(test_board, 'X'))


def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


# print(space_check(test_board, 2))


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_position = 0

    while not space_check(board, player_position):
        player_position = random.choice(positions)

    return player_position


def replay():
    return input("do you want to play again? Yes or No: ").lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # reset board and set up a game here
    the_board = [" "] * 10
    player_1_marker, player_2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first")

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == "Player 1":
            display_board(the_board)
            gamer_position = player_choice(the_board)
            place_marker(the_board, player_1_marker, gamer_position)

            if win_check(the_board, player_1_marker):
                display_board(the_board)
                print("Congratulations to Player 1 you won")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        # Player2's turn.
        else:
            display_board(the_board)
            gamer_position = player_choice(the_board)
            place_marker(the_board, player_2_marker, gamer_position)

            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print("Congratulations to Player 2 you won")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
