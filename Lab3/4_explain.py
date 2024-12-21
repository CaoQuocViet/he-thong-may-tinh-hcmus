Dưới đây là phần giải thích chi tiết từng bước trong thuật toán Minimax được triển khai trong mã nguồn của trò chơi Tic-Tac-Toe. Mỗi phần của thuật toán sẽ được giải thích cùng với đoạn mã tương ứng và ánh xạ đến lý thuyết về Minimax.

Định Nghĩa và Khởi Tạo
Mã Nguồn:

python
Sao chép mã
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
Giải Thích:

HUMAN và COMP là các hằng số đại diện cho hai người chơi trong trò chơi: người chơi (học sinh) và máy tính (máy tính).
board là bàn cờ 3x3, với giá trị 0 đại diện cho ô trống, +1 cho máy tính và -1 cho người chơi.
Hàm evaluate
Mã Nguồn:

python
Sao chép mã
def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score
Giải Thích:

evaluate đánh giá trạng thái hiện tại của bàn cờ. Nếu máy tính thắng (COMP), trả về +1. Nếu người chơi thắng (HUMAN), trả về -1. Nếu không có ai thắng, trả về 0. Đây là giá trị điểm cho trạng thái của trò chơi, giúp thuật toán Minimax quyết định nước đi tốt nhất.
Hàm wins
Mã Nguồn:

python
Sao chép mã
def wins(state, player):
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
    if [player, player, player] in win_state:
        return True
    else:
        return False
Giải Thích:

wins kiểm tra nếu người chơi cụ thể (player) có chiến thắng hay không. Nó xác minh tất cả các đường (hàng, cột, chéo) để xem liệu có ba ký tự liên tiếp của người chơi đó không. Đây là cơ sở để xác định trạng thái kết thúc trò chơi trong thuật toán Minimax.
Hàm game_over
Mã Nguồn:

python
Sao chép mã
def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)
Giải Thích:

game_over kiểm tra nếu trò chơi đã kết thúc, tức là một trong hai người chơi đã thắng. Nếu một trong hai người chơi thắng, trò chơi kết thúc.
Hàm empty_cells
Mã Nguồn:

python
Sao chép mã
def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells
Giải Thích:

empty_cells trả về danh sách các ô còn trống trên bàn cờ. Đây là thông tin quan trọng để thuật toán Minimax có thể thử tất cả các nước đi khả thi.
Hàm valid_move
Mã Nguồn:

python
Sao chép mã
def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False
Giải Thích:

valid_move kiểm tra xem một ô cụ thể có phải là ô trống và hợp lệ để thực hiện nước đi không.
Hàm set_move
Mã Nguồn:

python
Sao chép mã
def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False
Giải Thích:

set_move thực hiện nước đi của người chơi vào ô (x, y) nếu nó hợp lệ. Đây là cách cập nhật bàn cờ với nước đi mới.
Hàm minimax
Mã Nguồn:

python
Sao chép mã
def minimax(state, depth, player):
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
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best
Giải Thích:

Khởi tạo: best là danh sách lưu trữ kết quả tốt nhất cho người chơi hiện tại. Nếu là máy tính (COMP), điểm bắt đầu là -infinity (vì máy tính muốn điểm cao nhất). Nếu là người chơi (HUMAN), điểm bắt đầu là +infinity (vì người chơi muốn điểm thấp nhất).

Trường hợp cơ bản: Nếu depth bằng 0 (tức là không còn nước đi khả thi) hoặc trò chơi đã kết thúc (game_over), hàm evaluate đánh giá trạng thái hiện tại và trả về điểm số.

Tìm nước đi tốt nhất: Hàm kiểm tra tất cả các nước đi khả thi, thực hiện nước đi đó, gọi đệ quy minimax để tìm điểm số cho nước đi đó, và hoàn tác nước đi.

Nếu là máy tính (COMP), chọn nước đi với điểm số cao nhất.
Nếu là người chơi (HUMAN), chọn nước đi với điểm số thấp nhất.
Hàm ai_turn và human_turn
Mã Nguồn ai_turn:

python
Sao chép mã
def ai_turn(c_choice, h_choice):
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
Giải Thích:

Chiến lược của máy tính: Máy tính gọi minimax để tìm nước đi tốt nhất trừ khi bàn cờ đầy, trong trường hợp đó, nó chọn ngẫu nhiên một nước đi. Hàm minimax trả về nước đi tối ưu và máy tính thực hiện nước đi đó.
Mã Nguồn human_turn:

python
Sao chép mã
def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

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
Giải Thích:

Chiến lược của người chơi: Người chơi chọn nước đi bằng cách nhập số từ bàn phím. Nước đi sẽ được thực hiện nếu nó hợp lệ. Nếu không hợp lệ, người chơi sẽ phải chọn lại.
Hàm main



Bạn đã nói:
tiếp tục
ChatGPT đã nói:
ChatGPT
Hàm main
Mã Nguồn:

python
Sao chép mã
def main():
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

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
Giải Thích:

Khởi tạo lựa chọn của người chơi và máy tính:

python
Sao chép mã
h_choice = ''  # X or O
c_choice = ''  # X or O
Đặt lựa chọn của người chơi và máy tính. Người chơi sẽ chọn giữa X và O. Máy tính sẽ được gán ký tự còn lại.
Nhập lựa chọn của người chơi:

python
Sao chép mã
while h_choice != 'O' and h_choice != 'X':
    try:
        print('')
        h_choice = input('Choose X or O\nChosen: ').upper()
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()
    except (KeyError, ValueError):
        print('Bad choice')
Yêu cầu người chơi nhập X hoặc O cho nước đi của mình. Xử lý các lỗi đầu vào không hợp lệ.
Xác định ký tự của máy tính:

python
Sao chép mã
if h_choice == 'X':
    c_choice = 'O'
else:
    c_choice = 'X'
Nếu người chơi chọn X, máy tính sẽ chọn O, và ngược lại.
Xác định ai sẽ đi trước:

python
Sao chép mã
while first != 'Y' and first != 'N':
    try:
        first = input('First to start?[y/n]: ').upper()
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()
    except (KeyError, ValueError):
        print('Bad choice')
Hỏi người chơi xem họ muốn bắt đầu trước không. Xử lý các lỗi đầu vào không hợp lệ.
Vòng lặp trò chơi:

python
Sao chép mã
while len(empty_cells(board)) > 0 and not game_over(board):
    if first == 'N':
        ai_turn(c_choice, h_choice)
        first = ''
    human_turn(c_choice, h_choice)
    ai_turn(c_choice, h_choice)
Nếu còn ô trống và trò chơi chưa kết thúc, máy tính và người chơi lần lượt thực hiện các nước đi. Nếu người chơi không đi trước (first == 'N'), máy tính sẽ đi trước.
Xử lý kết quả của trò chơi:

python
Sao chép mã
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
Kiểm tra kết quả của trò chơi sau khi kết thúc vòng lặp. Nếu người chơi thắng, máy tính thắng, hoặc trò chơi hòa, thông báo kết quả tương ứng.
Kết thúc chương trình:

python
Sao chép mã
exit()
Kết thúc chương trình khi trò chơi đã hoàn tất.
Tóm Tắt và Ánh Xạ đến Lý Thuyết Minimax
Khái Niệm Cơ Bản:

Minimax là thuật toán tìm kiếm đệ quy giúp người chơi MAX (máy tính) tối đa hóa điểm số của mình và người chơi MIN (người chơi) tối thiểu hóa điểm số của đối thủ. Thuật toán này đánh giá tất cả các nước đi khả thi và chọn nước đi tốt nhất dựa trên điểm số do hàm evaluate cung cấp.
Thuật Toán Minimax:

Khởi tạo: Xác định giá trị điểm khởi đầu cho máy tính và người chơi.
Trường hợp cơ bản: Đánh giá trạng thái hiện tại khi không còn nước đi hoặc trò chơi đã kết thúc.
Tìm kiếm: Thử tất cả các nước đi khả thi, gọi đệ quy để tìm điểm số, và chọn nước đi tối ưu dựa trên điểm số.
Hiệu Suất:

Thuật toán Minimax là cơ bản và hiệu quả cho các trò chơi đơn giản như Tic-Tac-Toe. Đối với các trò chơi phức tạp hơn, thuật toán Minimax có thể được tối ưu hóa bằng cách sử dụng phương pháp cắt tỉa alpha-beta để giảm số lượng trạng thái cần đánh giá.
Mã nguồn này là một ví dụ điển hình về cách thuật toán Minimax được áp dụng trong trò chơi hai người, cung cấp một cách tiếp cận đơn giản nhưng mạnh mẽ để xây dựng một AI có khả năng chơi Tic-Tac-Toe một cách tối ưu.




=========================================================================================================
=========================================================================================================




Thuật toán Minimax là một thuật toán tìm kiếm trong trò chơi hai người đối kháng, nơi mục tiêu là tối đa hóa lợi ích cho bên chơi (MAX) và tối thiểu hóa thiệt hại cho đối thủ (MIN). Đây là một thuật toán đệ quy, hoạt động trên một cây trò chơi biểu diễn các trạng thái của trò chơi và các nước đi có thể. Mỗi nút của cây biểu thị một trạng thái của bàn cờ, với các nút con biểu thị các trạng thái tiếp theo sau mỗi nước đi của người chơi.

Các hàm chính trong code và cách chúng ánh xạ tới thuật toán Minimax:
evaluate(state):

Hàm này đánh giá trạng thái hiện tại của bàn cờ.
Trả về +1 nếu máy tính thắng, -1 nếu con người thắng, và 0 nếu hòa.
Nó được sử dụng để đánh giá các trạng thái kết thúc của trò chơi, giúp Minimax quyết định nước đi tối ưu.
wins(state, player):

Hàm này kiểm tra xem một người chơi cụ thể đã thắng hay chưa.
Dựa trên các hàng, cột và đường chéo trên bàn cờ để kiểm tra xem có ba ký tự liên tiếp của người chơi đó không.
game_over(state):

Hàm này kiểm tra xem trò chơi đã kết thúc chưa bằng cách kiểm tra xem người chơi nào đó đã thắng.
minimax(state, depth, player):

Đây là hàm chính thực hiện thuật toán Minimax.
Nó dựa vào thực tế rằng một nước đi tối ưu cho MAX là nước đi tối đa giá trị của các nước đi con của nó (MIN sẽ cố gắng tối thiểu giá trị).
Đệ quy duyệt qua tất cả các nước đi có thể, đánh giá điểm số cho từng nước đi và trả về nước đi tốt nhất cho độ sâu hiện tại.
ai_turn(c_choice, h_choice):

Hàm này thực hiện lượt đi của máy tính.
Nếu độ sâu là 9 (bàn cờ trống), nó chọn một nước đi ngẫu nhiên.
Ngược lại, nó gọi hàm minimax để chọn nước đi tối ưu dựa trên độ sâu hiện tại của bàn cờ.
human_turn(c_choice, h_choice):

Hàm này cho phép người chơi điều khiển.
Người chơi nhập vị trí trên bàn cờ và hàm kiểm tra tính hợp lệ của nước đi.
Sau đó, nó gọi hàm set_move để thực hiện nước đi của người chơi.
Cây trò chơi (Game Tree):
Cây trò chơi là một biểu đồ đồ thị hướng, biểu diễn tất cả các trạng thái có thể của trò chơi và các hành động có thể được thực hiện từ mỗi trạng thái. Trong trò chơi Tic-Tac-Toe, cây trò chơi có thể rất đơn giản với các mức sâu hữu hạn do bàn cờ có kích thước nhỏ.

Tối ưu hóa và cắt tỉa Alpha-Beta:
Trong trường hợp các trò chơi phức tạp hơn như cờ vua, thuật toán Minimax có thể trở nên chậm vì phải duyệt qua nhiều nút của cây trò chơi. Cắt tỉa Alpha-Beta là một kỹ thuật tối ưu hóa giúp loại bỏ các nhánh của cây trò chơi mà không cần duyệt, dẫn đến tăng tốc đáng kể thuật toán Minimax.

Tóm tắt:
Thuật toán Minimax là một phương pháp hiệu quả để lập kế hoạch nước đi cho máy tính trong các trò chơi đối kháng. Bằng cách duyệt qua các nút của cây trò chơi và sử dụng hàm evaluate để đánh giá các trạng thái kết thúc, nó giúp máy tính đưa ra quyết định nước đi tối ưu dựa trên chiến lược tối ưu hóa lợi ích và thiệt hại.