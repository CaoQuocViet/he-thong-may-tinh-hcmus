// Nhap xuat mang 1 chieu n so nguyen

.extern printf
.extern scanf

.section .data
    tb1: .asciz "Nhap vao so n: "
    tb2: .asciz "a[%d]: "
    tb3: .asciz "Mang vua nhap la: \n"
    fmt1: .asciz "%d"
    fmt2: .asciz "%d\n"

.section .bss
    n: .space 4         
    arr: .space 400 

.section .text
.global main
main:
    // Xuat tb1
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    // Nhap n
    adrp x0, fmt1
    add x0, x0, :lo12:fmt1
    adrp x1, n
    add x1, x1, :lo12:n
    bl scanf

    // Load n vao x19
    adrp x19, n
    add x19, x19, :lo12:n
    ldur x19, [x19]

    // Load dia chi mang vao x20
    adrp x20, arr
    add x20, x20, :lo12:arr

    // Khoi tao vong lap
    mov x9, #0 // i = 0

Lap_Nhap:
    // Xuat tb2
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    mov x1, x9
    bl printf

    // Nhap arr[i]
    adrp x0, fmt1
    add x0, x0, :lo12:fmt1
    mov x1, x20
    bl scanf

    // Tang dia chi mang
    add x20, x20, #8

    // Tang i
    add x9, x9, #1

    // Kiem tra i < n thi lap lai
    cmp x9, x19
    b.lt Lap_Nhap

    // Xuat tb3
    adrp x0, tb3
    add x0, x0, :lo12:tb3
    bl printf

    // Load dia chi mang vao x20 (do sau khi nhap thi no nhay ve cuoi mang)
    adrp x20, arr
    add x20, x20, :lo12:arr

    // Khoi tao vong lap
    mov x9, #0 // i = 0

Lap_Xuat:
    // Xuat arr[i]
    adrp x0, fmt2
    add x0, x0, :lo12:fmt2
    ldur x1, [x20]
    bl printf

    // Tang dia chi mang
    add x20, x20, #8

    // Tang i
    add x9, x9, #1

    // Kiem tra i < n thi lap lai
    cmp x9, x19
    b.lt Lap_Xuat

    // Ket thuc chuong trinh
    mov x0, #0
    mov x8, #93
    svc #0