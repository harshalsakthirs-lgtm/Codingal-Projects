import random
from tabnanny import check

from colorama import Fore, init, Style

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
                return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print('' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---------' + Style.RESET_ALL)
    print('' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---------' + Style.RESET_ALL)
    print('' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input("Do you want to be 'X' or 'O': ")
        if symbol == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or board[move - 1].isdigit():
        try:
            move - int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please neter a number (1 - 9)")

    board[move - 1] = symbol


def ai_move(board, ai_symbol, player_symbol):
    for h in range(9):
        if board[h].isdigit():
            board_copy = board.copy()
            board_copy[h] = ai_symbol
            if check_win (board_copy, ai_symbol):
                board[h] = ai_symbol
                return
    for h in range(9):
        if board[h].isdigit():
            board_copy = board.copy()
            board_copy[h] = player_symbol
            if check_win(board_copy, player_symbol):
                board[h] = ai_symbol
                return


    possible_moves = [h for h in range(9) if board[h].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol


def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
        return False


def check_full(board):
    return all(not spot.isdigit() for spot in board )


def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.BLUE + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_name, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            