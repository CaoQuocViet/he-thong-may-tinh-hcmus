.extern scanf
.extern printf

.section .data
    tb1: .asciz "Nhap ho ten: "
    tb2: .asciz "Nhap nam sinh: "
    tb3: .asciz "Xin chao %s!\nTuoi: %d\n" // Chi xuat khong nhap nen phai co /n
    fmt: .asciz "%s"
    fmt2: .asciz "%d"
    // namsinh va tuoi word 0 thi khong loi, word 1 thi loi
    // nen de namsinh va tuoi la word 0 va dat o .data

.section .bss
    hoten: .space 30
    namsinh: .word 0 // Nen de o .data
    tuoi: .word 0 // Nen de o .data

.section .text
.global main
main:
    // Xuat tb1
    adrp x0, tb1
    add x0, x0, :lo12:tb1
    bl printf

    // Nhap ho ten scanf("%s", hoten);
    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, hoten
    add x1, x1, :lo12:hoten
    bl scanf

    // Xuat tb2
    adrp x0, tb2
    add x0, x0, :lo12:tb2
    bl printf

    // Nhap nam sinh scanf("%d", &namsinh);
    adrp x0, fmt2
    add x0, x0, :lo12:fmt2
    adrp x1, namsinh
    add x1, x1, :lo12:namsinh
    bl scanf

    // Tinh tuoi
    mov x9, #2024  // Năm hiện tại

    // Load namsinh vao x10
    adrp x10, namsinh
    add x10, x10, :lo12:namsinh
    ldr w10, [x10]  // Đọc dữ liệu 32-bit từ namsinh

    // Tinh tuoi
    sub x11, x9, x10

    // Xuat tb3 printf("Xin chao %s!\nTuoi: %d\n", hoten, tuoi);
    adrp x0, tb3
    add x0, x0, :lo12:tb3
    adrp x1, hoten
    add x1, x1, :lo12:hoten
    mov x2, x11
    bl printf

    // Thoat chuong trinh
    mov x0, #0
    mov x8, #93
    svc #0