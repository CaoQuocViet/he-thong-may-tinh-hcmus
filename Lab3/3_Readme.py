Tic-Tac-Toe Minimax

Giới thiệu: Đây là một cài đặt thuật toán Minimax cho trò chơi Tic-Tac-Toe (hay còn gọi là Cờ Caro). Minimax là một thuật toán trí tuệ nhân tạo được sử dụng để tìm nước đi tốt nhất trong các trò chơi hai người như Tic-Tac-Toe, Cờ Vây, và Cờ Tướng.

Khái Niệm: Để giải quyết trò chơi bằng AI, chúng ta sử dụng khái niệm "cây trò chơi" và thuật toán Minimax. Cây trò chơi đại diện cho các trạng thái của trò chơi, với mỗi trạng thái là một nút trong cây. Nút gốc (root) của cây biểu thị vị trí bắt đầu của trò chơi (bàn cờ còn trống). Các nút trên các cấp tiếp theo đại diện cho các trạng thái có thể xảy ra sau mỗi nước đi của người chơi. Những nút này được gọi là "con" của nút gốc.

Mỗi nút trên một cấp sẽ có các nút con là các trạng thái có thể đạt được từ nó bởi nước đi của đối thủ. Quá trình này tiếp tục cho đến khi đạt đến các trạng thái kết thúc trò chơi, nghĩa là hoặc một người chơi thắng (có ba ký hiệu liên tiếp) hoặc bàn cờ đầy và trò chơi kết thúc hòa.

Minimax Là Gì? Minimax là một thuật toán trí tuệ nhân tạo được áp dụng trong các trò chơi hai người như Tic-Tac-Toe, Cờ Caro, Cờ Vua, và Go. Những trò chơi này được gọi là "trò chơi tổng bằng 0" (zero-sum games) vì trong mô hình toán học, khi một người thắng (+1), người kia thua (-1) hoặc cả hai đều không thắng (0).

Thuật Toán Hoạt Động Như Thế Nào? Thuật toán tìm kiếm nước đi tốt nhất một cách đệ quy nhằm giúp người chơi MAX (máy tính) thắng hoặc ít nhất không thua (hòa). Thuật toán xem xét trạng thái hiện tại của trò chơi và các nước đi khả thi tại trạng thái đó. Đối với mỗi nước đi hợp lệ, thuật toán tiếp tục (hoán đổi giữa MAX và MIN) cho đến khi tìm được trạng thái kết thúc (thắng, hòa hoặc thua).

Hiểu Thuật Toán: Thuật toán Minimax có thể được mô tả bằng pseudocode như sau:

python
Sao chép mã
minimax(state, depth, player)

    if (player = max) then
        best = [null, -infinity]
    else
        best = [null, +infinity]

    if (depth = 0 or gameover) then
        score = evaluate this state for player
        return [null, score]

    for each valid move m for player in state s do
        execute move m on s
        [move, score] = minimax(s, depth - 1, -player)
        undo move m on s

        if (player = max) then
            if score > best.score then best = [move, score]
        else
            if score < best.score then best = [move, score]

    return best
end
Giải Thích Mã Python:

Khởi Tạo:

python
Sao chép mã
board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
MAX = +1
MIN = -1
Bàn cờ là ma trận 3x3, với MAX và MIN đại diện cho hai người chơi. MAX có thể là X hoặc O và MIN là ngược lại.

Hàm minimax:

python
Sao chép mã
def minimax(state, depth, player):
    if player == MAX:
        return [-1, -1, -infinity]
    else:
        return [-1, -1, +infinity]
Cả hai người chơi bắt đầu với điểm số xấu nhất. Nếu là MAX, điểm số bắt đầu là -∞, và nếu là MIN, điểm số bắt đầu là +∞.

Trường Hợp Cơ Bản:

python
Sao chép mã
if depth == 0 or game_over(state):
    score = evaluate(state)
    return [-1, -1, score]
Nếu độ sâu bằng 0 hoặc trò chơi đã kết thúc, hàm evaluate sẽ đánh giá trạng thái hiện tại và trả về điểm số.

Tìm Nước Đi Tốt Nhất:

python
Sao chép mã
for cell in empty_cells(state):
    x, y = cell[0], cell[1]
    state[x][y] = player
    score = minimax(state, depth - 1, -player)
    state[x][y] = 0
    score[0], score[1] = x, y
Đối với mỗi nước đi hợp lệ, thuật toán sẽ thực hiện nước đi đó, gọi đệ quy hàm minimax để đánh giá điểm số, và sau đó hoàn tác nước đi. Nước đi tốt nhất sẽ được chọn dựa trên điểm số.

So Sánh Điểm Số:

python
Sao chép mã
if player == MAX:
    if score[2] > best[2]:
        best = score
else:
    if score[2] < best[2]:
        best = score
Đối với MAX, điểm số lớn hơn sẽ được ưu tiên. Đối với MIN, điểm số nhỏ hơn sẽ được ưu tiên.

Cây Trò Chơi: Cây trò chơi giúp hình dung các nước đi và trạng thái của trò chơi. Trong ví dụ đơn giản, nước đi tốt nhất nằm ở giữa vì giá trị lớn nhất nằm ở nút thứ hai bên trái. Cây trò chơi đầy đủ có thể rất phức tạp; ví dụ, cây trò chơi đầy đủ cho Tic-Tac-Toe có 549.946 nút.

Tối Ưu Hóa Thuật Toán: Trong các trò chơi phức tạp như cờ vua, việc tìm kiếm toàn bộ cây trò chơi là khó khăn. Tuy nhiên, thuật toán Cắt Tỉa Alpha-Beta là một phương pháp tối ưu hóa cho thuật toán Minimax, cho phép loại bỏ một số nhánh không cần thiết trong cây tìm kiếm.