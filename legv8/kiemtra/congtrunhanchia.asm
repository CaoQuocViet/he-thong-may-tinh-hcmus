.extern printf
.extern scanf

.section .data
    fmt: .asciz "%d"
    menu: .asciz "==== Menu =====\n1. Tong\n2. Hieu\n3. Tich\n4. Thuong\n5. Thoat\n================\nChon: "
    prompt_a: .asciz "Nhap vao so a: "
    prompt_b: .asciz "Nhap vao so b: "
    result_sum: .asciz "%d + %d = %d\n"
    result_diff: .asciz "%d - %d = %d\n"
    result_prod: .asciz "%d * %d = %d\n"
    result_quot: .asciz "%d / %d = %d\n"
    invalid: .asciz "Lua chon khong hop le.\n"
    invalid_division: .asciz "Khong the chia cho 0.\n"

.section .bss
    a: .dword 0
    b: .dword 0
    choice: .dword 0

.section .text
.global main

main:
    // Nhap so a
    adrp x0, prompt_a
    add x0, x0, :lo12:prompt_a
    bl printf

    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, a
    add x1, x1, :lo12:a
    bl scanf

    // Nhap so b
    adrp x0, prompt_b
    add x0, x0, :lo12:prompt_b
    bl printf

    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, b
    add x1, x1, :lo12:b
    bl scanf

menu_loop:
    // Xuat menu
    adrp x0, menu
    add x0, x0, :lo12:menu
    bl printf

    // Nhap lua chon
    adrp x0, fmt
    add x0, x0, :lo12:fmt
    adrp x1, choice
    add x1, x1, :lo12:choice
    bl scanf

    // Load lua chon
    adrp x19, choice
    add x19, x19, :lo12:choice
    ldur x19, [x19] // choice

    // Xử lý lựa chọn
    cmp x19, #1
    beq calculate_sum
    cmp x19, #2
    beq calculate_diff
    cmp x19, #3
    beq calculate_product
    cmp x19, #4
    beq calculate_quotient
    cmp x19, #5
    beq exit_program

    // Lua chon khong hop le
    adrp x0, invalid
    add x0, x0, :lo12:invalid
    bl printf
    b menu_loop

calculate_sum:
    // Tinh tong a + b
    adrp x1, a
    add x1, x1, :lo12:a
    ldur x1, [x1] // a

    adrp x2, b
    add x2, x2, :lo12:b
    ldur x2, [x2] // b

    add x0, x1, x2 // res = a + b
    // In ra kết quả
    adrp x0, result_sum
    add x0, x0, :lo12:result_sum
    mov x1, x1 // a
    mov x2, x2 // b
    mov x3, x0 // res
    bl printf
    b menu_loop

calculate_diff:
    // Tinh hieu a - b
    adrp x1, a
    add x1, x1, :lo12:a
    ldur x1, [x1] // a

    adrp x2, b
    add x2, x2, :lo12:b
    ldur x2, [x2] // b

    sub x0, x1, x2 // res = a - b
    // In ra kết quả
    adrp x0, result_diff
    add x0, x0, :lo12:result_diff
    mov x1, x1 // a
    mov x2, x2 // b
    mov x3, x0 // res
    bl printf
    b menu_loop

calculate_product:
    // Tinh tich a * b
    adrp x1, a
    add x1, x1, :lo12:a
    ldur x1, [x1] // a

    adrp x2, b
    add x2, x2, :lo12:b
    ldur x2, [x2] // b

    mul x0, x1, x2 // res = a * b
    // In ra kết quả
    adrp x0, result_prod
    add x0, x0, :lo12:result_prod
    mov x1, x1 // a
    mov x2, x2 // b
    mov x3, x0 // res
    bl printf
    b menu_loop

calculate_quotient:
    // Tinh thuong a / b
    adrp x1, a
    add x1, x1, :lo12:a
    ldur x1, [x1] // a

    adrp x2, b
    add x2, x2, :lo12:b
    ldur x2, [x2] // b

    // Kiểm tra b != 0
    cmp x2, #0
    beq print_invalid_division // Nếu b == 0 thì báo lỗi

    sdiv x0, x1, x2 // res = a / b
    // In ra kết quả
    adrp x0, result_quot
    add x0, x0, :lo12:result_quot
    mov x1, x1 // a
    mov x2, x2 // b
    mov x3, x0 // res
    bl printf
    b menu_loop


print_invalid_division:
    adrp x0, invalid_division
    add x0, x0, :lo12:invalid_division
    bl printf
    b menu_loop

exit_program:
    // Kết thúc chương trình
    mov x0, #0
    mov x8, #93
    svc #0
