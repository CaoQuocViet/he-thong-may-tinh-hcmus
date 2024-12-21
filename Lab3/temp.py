#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMP = +1
board = []
size = 3  # Default size is 3x3
win_length = 3  # Default win length is 3

def evaluate(state):
    """
    Heuristic evaluation of the state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 for draw
    """
    if wins(state, COMP):
        return +1
    elif wins(state, HUMAN):
        return -1
    return 0

def wins(state, player):
    """
    Checks if the player has won based on the current win_length.
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    def check_line(line):
        return [player] * win_length in [line[i:i + win_length] for i in range(len(line) - win_length + 1)]

    # Check rows and columns
    for i in range(size):
        if check_line(state[i]) or check_line([state[j][i] for j in range(size)]):
            return True

    # Check diagonals
    for i in range(size - win_length + 1):
        if (check_line([state[i + j][j] for j in range(size - i)]) or
            check_line([state[j][i + j] for j in range(size - i)])):
            return True
        if (check_line([state[i + j][size - 1 - j] for j in range(size - i)]) or
            check_line([state[j][size - 1 - (i + j)] for j in range(size - i)])):
            return True

    return False

def game_over(state):
    """
    Checks if the game is over.
    :param state: the state of the current board
    :return: True if the game is over
    """
    return wins(state, HUMAN) or wins(state, COMP) or len(empty_cells(state)) == 0

def empty_cells(state):
    """
    Returns a list of empty cells.
    :param state: the state of the current board
    :return: a list of empty cells
    """
    return [[x, y] for x, row in enumerate(state) for y, cell in enumerate(row) if cell == 0]

def valid_move(x, y):
    """
    Checks if a move is valid.
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    return [x, y] in empty_cells(board)

def set_move(x, y, player):
    """
    Sets a move on the board if the coordinates are valid.
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False

def minimax(state, depth, alpha, beta, player):
    """
    Minimax function with Alpha-Beta Pruning.
    :param state: current state of the board
    :param depth: current depth in the search tree
    :param alpha: alpha value for pruning
    :param beta: beta value for pruning
    :param player: a human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        return [-1, -1, evaluate(state)]

    for cell in empty_cells(state):
        x, y = cell
        state[x][y] = player
        score = minimax(state, depth - 1, alpha, beta, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, best[2])

        if beta <= alpha:
            break

    return best

def clean():
    """
    Clears the console.
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def render(state, c_choice, h_choice):
    """
    Prints the board on console in the specified format.
    :param state: current state of the board
    """
    chars = {
        HUMAN: h_choice,
        COMP: c_choice,
        0: ' '
    }

    # Create horizontal line based on board size
    horizontal_line = '-' * (size * 4 + 1 + (size - 1))  # 4 characters per cell: |   |, plus one for border

    # Print the board
    print('\n' + horizontal_line)
    for row in state:
        print('|' + '||'.join(f' {chars[cell]} ' for cell in row) + '|')
        print(horizontal_line)

def ai_turn(c_choice, h_choice):
    """
    Handles the computer's turn using Minimax with Alpha-Beta Pruning.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    """
    depth = min(len(empty_cells(board)), 3)
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == size * size:
        x, y = choice(range(size)), choice(range(size))
    else:
        move = minimax(board, depth, -infinity, infinity, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)

def human_turn(c_choice, h_choice):
    """
    Handles the human's turn.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    moves = {i + 1: [i // size, i % size] for i in range(size * size)}

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    move = -1
    while move < 1 or move > size * size:
        try:
            move = int(input(f'Use numpad (1..{size * size}): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

def initialize_board():
    """
    Initializes the board based on user input or default empty board.
    """
    global board
    print("Do you want to initialize the board with a custom state? (y/n)")
    choice = input().strip().lower()
    
    if choice == 'y':
        print(f"Enter the initial state of the {size}x{size} board (use 0 for empty, 1 for computer's move, -1 for human's move):")
        valid_input = False

        while not valid_input:
            try:
                user_input = input(f"Enter board state as a single line of {size * size} numbers (e.g., {' '.join(['0']*size*size)}): ")
                board_values = list(map(int, user_input.split()))
                
                if len(board_values) != size * size:
                    raise ValueError("You must enter exactly the correct number of values.")
                
                # Convert the flat list into a 2D board
                board = [board_values[i*size:(i+1)*size] for i in range(size)]
                
                human_count = sum(1 for row in board for cell in row if cell == HUMAN)
                comp_count = sum(1 for row in board for cell in row if cell == COMP)
                
                if abs(human_count - comp_count) > 1:
                    print("The number of moves for each player must not differ by more than 1.")
                else:
                    valid_input = True
            except (ValueError, IndexError):
                print("Invalid input. Please enter exactly the correct number of integers.")

    else:
        board = [[0] * size for _ in range(size)]

def main():
    """
    Main function that calls all functions.
    """
    global size, win_length

    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Choose board size
    valid_size = False
    while not valid_size:
        try:
            print("Choose board size (3x3, 5x5, 10x10, 20x20):")
            size_input = input().strip().lower()
            if size_input == '3x3':
                size = 3
            elif size_input == '5x5':
                size = 5
            elif size_input == '10x10':
                size = 10
            elif size_input == '20x20':
                size = 20
            else:
                raise ValueError("Invalid board size. Choose from 3x3, 5x5, 10x10, 20x20.")
            valid_size = True
        except ValueError as e:
            print(e)

    # Choose win length
    valid_win_length = False
    while not valid_win_length:
        try:
            print(f"Choose win length (3 or 5) for a {size}x{size} board:")
            win_length_input = int(input().strip())
            if win_length_input == 3 or (size >= 5 and win_length_input == 5):
                win_length = win_length_input
                valid_win_length = True
            else:
                raise ValueError("Invalid win length for the chosen board size.")
        except ValueError as e:
            print(e)

    initialize_board()

    # Human chooses X or O to play
    while h_choice not in ['O', 'X']:
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    c_choice = 'O' if h_choice == 'X' else 'X'

    # Determine who starts first
    clean()
    while first not in ['Y', 'N']:
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()

if __name__ == '__main__':
    main()
