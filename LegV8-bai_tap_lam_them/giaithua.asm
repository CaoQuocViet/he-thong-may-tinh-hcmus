.extern printf
.extern scanf

.section .data
    tb1: .asciz "Nhap x: "
    tb2: .asciz "Nhap n: "
    tb3: .asciz "x mu n (%d^%d) la: %d\n"
    fmt: .asciz "%d"

.section .bss
    x: .skip 4
    n: .skip 4
    result: .skip 4

.section .text
.global main

main:
    // Nhập x
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, x
    add x1, x1, :lo12:x
    bl scanf

    // Nhập n
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    bl printf

    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, n
    add x1, x1, :lo12:n
    bl scanf

    // Load x và n
    adrp x19, x
    add x19, x19, :lo12:x
    ldur x19, [x19] // x

    adrp x20, n
    add x20, x20, :lo12:n
    ldur x20, [x20] // n

    // Khởi tạo biến kết quả
    mov x21, #1       // result = 1
    mov x22, #0       // i = 0

power_loop:
    // Kiểm tra i < n
    cmp x22, x20
    b.ge end_power_loop // Nếu i >= n, thoát vòng lặp

    // result = result * x
    mul x21, x21, x19 // result *= x

    // i++
    add x22, x22, #1
    b power_loop

end_power_loop:
    // Lưu kết quả vào biến result
    adrp x23, result
    add x23, x23, :lo12:result
    stur x21, [x23] // lưu kết quả

    // Xuất kết quả
    adrp x0, tb3
    add x0, x0, :lo12:tb3
    mov x1, x19      // x
    mov x2, x20      // n
    mov x3, x21      // result
    bl printf

    // Kết thúc chương trình
    mov x0, #0
    mov x8, #93
    svc #0
