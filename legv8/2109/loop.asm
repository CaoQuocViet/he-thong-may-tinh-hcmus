// Nhap n, tinh tong 1 den n

.extern printf
.extern scanf

.section .data
    tb1: .asciz "Nhap vao so n: "
    tb2: .asciz "Tong 1 den n la: %d\n"
    fmt: .asciz "%d"
    // n: .dword 0
    // s: .dword 0
.section .bss
    n: .skip 4
    s: .skip 4

.section .text
.global main
main:
    // Xuat tb1
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    // Nhap n
    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, n
    add x1, x1, :lo12:n
    bl scanf

    // Load n vao x19
    adrp x19, n
    add x19, x19, :lo12:n
    ldur x19, [x19]

    // Khoi tao vong lap
    mov x20, #0 // s = 0
    mov x9, #1 // i = 1

Lap:
    add x20, x20, x9 // s = s + i
    add x9, x9, #1 // i = i + 1

    // Kiem tra i <= n thi lap lai
    cmp x9, x19
    b.le Lap

    // Luu x20 vao s
    adrp x9, s
    add x9, x9, :lo12:s
    str x20, [x9]

    // Xuat tb2
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    mov x1, x19
    mov x2, x20
    bl printf

    // Ket thuc chuong trinh
    mov x0, #0
    mov x8, #93
    svc #0