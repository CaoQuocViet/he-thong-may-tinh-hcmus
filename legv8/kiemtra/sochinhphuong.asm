.extern printf
.extern scanf

.section .data
    tb1: .asciz "Nhap n: "
    tb2: .asciz "N %d la so chinh phuong.\n"
    tb3: .asciz "N %d khong la so chinh phuong.\n"
    fmt: .asciz "%d"

.section .bss
    n: .dword 0
    sqrt: .dword 0
    square: .dword 0

.section .text
.global main

main:
    // Nhập n
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, n
    add x1, x1, :lo12:n
    bl scanf

    // Load n
    adrp x19, n
    add x19, x19, :lo12:n
    ldur x19, [x19] // n

    // Khởi tạo sqrt
    mov x20, #0 // sqrt = 0
    mov x21, #0 // square = 0
    mov x22, #1 // i = 1

check_loop:
    // Tính square = i * i
    mul x21, x22, x22 // square = i * i

    // Kiểm tra xem square có bằng n không
    cmp x21, x19
    beq is_perfect_square // Nếu square == n, nhảy đến is_perfect_square
    cmp x21, x19
    b.gt not_perfect_square // Nếu square > n, nhảy đến not_perfect_square

    // i++
    add x22, x22, #1
    b check_loop

is_perfect_square:
    // In ra thông báo số chính phương
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    mov x1, x19 // n
    bl printf
    b end_program

not_perfect_square:
    // In ra thông báo không phải số chính phương
    adrp x0, tb3
    add x0, x0, :lo12:tb3
    mov x1, x19 // n
    bl printf

end_program:
    // Kết thúc chương trình
    mov x0, #0
    mov x8, #93
    svc #0