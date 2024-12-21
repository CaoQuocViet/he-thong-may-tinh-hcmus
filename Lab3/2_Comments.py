#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Một cài đặt thuật toán AI Minimax trong trò chơi Tic Tac Toe,
sử dụng Python.
Phần mềm này được cấp phép dưới giấy phép GPL.
Tác giả: Clederson Cruz
Năm: 2017
Giấy phép: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1  # Đại diện cho người chơi, giá trị -1
COMP = +1   # Đại diện cho máy tính, giá trị +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    # Ma trận 3x3 đại diện cho bàn cờ Tic Tac Toe, với 0 nghĩa là ô trống
]

def evaluate(state):
    """
    Hàm đánh giá trạng thái bàn cờ.
    :param state: trạng thái hiện tại của bàn cờ
    :return: +1 nếu máy tính thắng; -1 nếu người chơi thắng; 0 nếu hòa
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):
    """
    Hàm kiểm tra xem một người chơi cụ thể có thắng không. Có các khả năng:
    * Ba hàng    [X X X] hoặc [O O O]
    * Ba cột     [X X X] hoặc [O O O]
    * Hai đường chéo [X X X] hoặc [O O O]
    :param state: trạng thái hiện tại của bàn cờ
    :param player: người chơi hoặc máy tính
    :return: True nếu người chơi thắng
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

def game_over(state):
    """
    Hàm kiểm tra xem trò chơi đã kết thúc chưa
    :param state: trạng thái hiện tại của bàn cờ
    :return: True nếu người chơi hoặc máy tính thắng
    """
    return wins(state, HUMAN) or wins(state, COMP)

def empty_cells(state):
    """
    Lấy danh sách các ô còn trống
    :param state: trạng thái hiện tại của bàn cờ
    :return: danh sách các ô còn trống
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def valid_move(x, y):
    """
    Một nước đi là hợp lệ nếu ô chọn còn trống
    :param x: tọa độ X
    :param y: tọa độ Y
    :return: True nếu board[x][y] còn trống
    """
    return [x, y] in empty_cells(board)

def set_move(x, y, player):
    """
    Đặt nước đi trên bàn cờ nếu tọa độ hợp lệ
    :param x: tọa độ X
    :param y: tọa độ Y
    :param player: người chơi hiện tại
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False

def minimax(state, depth, player):
    """
    Hàm AI chọn nước đi tốt nhất
    :param state: trạng thái hiện tại của bàn cờ
    :param depth: chỉ số nút trong cây (0 <= depth <= 9), nhưng không bao giờ bằng chín trong trường hợp này
    :param player: người chơi hoặc máy tính
    :return: danh sách với [hàng tốt nhất, cột tốt nhất, điểm tốt nhất]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # giá trị lớn nhất
        else:
            if score[2] < best[2]:
                best = score  # giá trị nhỏ nhất

    return best

def clean():
    """
    Xóa màn hình console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def render(state, c_choice, h_choice):
    """
    In bàn cờ ra console
    :param state: trạng thái hiện tại của bàn cờ
    """
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

def ai_turn(c_choice, h_choice):
    """
    Gọi hàm minimax nếu độ sâu < 9, ngược lại chọn tọa độ ngẫu nhiên.
    :param c_choice: sự lựa chọn của máy tính X hoặc O
    :param h_choice: sự lựa chọn của người chơi X hoặc O
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)

def human_turn(c_choice, h_choice):
    """
    Người chơi thực hiện một nước đi hợp lệ.
    :param c_choice: sự lựa chọn của máy tính X hoặc O
    :param h_choice: sự lựa chọn của người chơi X hoặc O
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Từ điển các nước đi hợp lệ
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
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

def main():
    """
    Hàm chính gọi tất cả các hàm
    """
    clean()
    h_choice = ''  # X hoặc O
    c_choice = ''  # X hoặc O
    first = ''  # nếu người chơi là người bắt đầu

    # Người chơi chọn X hoặc O để chơi
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Đặt sự lựa chọn của máy tính
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Người chơi có thể bắt đầu trước
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Vòng lặp chính của trò chơi
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Thông báo kết thúc trò chơi
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
