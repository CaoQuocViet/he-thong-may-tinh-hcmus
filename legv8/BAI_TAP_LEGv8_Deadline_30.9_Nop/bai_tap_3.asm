// Viết chương trình nhập vào số nguyên n. Kiểm tra n có là số chính phương hay không ?
.extern printf
.extern scanf

.section .data
    msg_info:                .asciz "Nhập số nguyên n: "
    msg_not_perfect_square:  .asciz "Số %ld không phải là số chính phương.\n"
    msg_perfect_square:      .asciz "Số %ld là số chính phương.\n"
    msg_integer:             .asciz "%ld"
    num:                     .dword 0

.section .text

.global main

main:	
    adrp x0, msg_info
    add x0, x0, :lo12:msg_info
    bl printf
	
    adrp x0, msg_integer
    add x0, x0, :lo12:msg_integer
    adrp x1, num
    add x1, x1, :lo12:num
    bl scanf
	
    adrp x9, num
    add x9, x9, :lo12:num	
    ldur x9, [x9]
	
    cmp x9, #1
    b.lt not_perfect_square
    b.eq perfect_square

    mov x10, #2
	
loop_start:
    lsl x11, x10, #1
    cmp x11, x9
    b.gt not_perfect_square
	
    mul x11, x10, x10
    cmp x11, x9
    b.eq perfect_square
	
    add x10, x10, #1
    b loop_start
	
perfect_square:
    adrp x0, msg_perfect_square
    add x0, x0, :lo12:msg_perfect_square
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
    b end
	
not_perfect_square:
    adrp x0, msg_not_perfect_square
    add x0, x0, :lo12:msg_not_perfect_square
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
	
end:
    mov x0, #0
    mov x8, #93
    svc #0
