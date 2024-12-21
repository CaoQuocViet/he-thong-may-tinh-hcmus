// Chuong trinh legv8
// Nhap vao 2 so a, b. Tinh tong, hieu, tich, thuong a va b

.extern printf
.extern scanf

.section .data
    tb1: .asciz "Nhap vao so a: "
    tb2: .asciz "Nhap vao so b: "
    menu: .asciz "==== menu =====\n1. Tong\n2. Hieu\n3. Tich\n4. Thuong\n5. Thoat\n================\nChon: "
    tb3: .asciz "%d %c %d = %d\n"
    fmt: .asciz "%d"

.section .bss
    a: .skip 4
    b: .skip 4
    c: .skip 4
    chon: .skip 4

.section .text
.global main
main:
    // Xuat tb1
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    // Nhap a
    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, a
    add x1, x1, :lo12:a
    bl scanf
    
    // Xuat tb2
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    bl printf

    // Nhap b
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    bl printf

    // Xuat menu
    adrp x0, menu
    add x0, x0, :lo12:menu
    bl printf

    // Nhap chon
    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, chon
    add x1, x1, :lo12:chon
    bl scanf

    // Load chon vao x19
    adrp x19, chon
    add x19, x19, :lo12:chon
    ldur x19, [x19]

    // Load x20 = a
    adrp x20, a
    add x20, x20, :lo12:a
    ldur x20, [x20]

    // Load x21 = b
    adrp x21, b
    add x0, x0, :lo12:b
    ldur x21, [x0]

    // Load dia chi c vao x23
    adrp x22, c
    add x22, x22, :lo12:c

    cmp x19, #1
    b.eq Tong

Tong:
    // Tinh tong
    add x23, x20, x21 // x23 = x20 + x21 (a + b)
    // Luu kq vao c
    stur x23, [x22]

    // Xuat tb3
    adrp x0, tb3
    add x0, x0, :lo12:tb3
    mov x1, x20
    mov x2, '+'
    mov x3, x21
    mov x4, x23
    bl printf

    // Ket thuc
    mov x0, #0
    mov x8, #93
    svc #0