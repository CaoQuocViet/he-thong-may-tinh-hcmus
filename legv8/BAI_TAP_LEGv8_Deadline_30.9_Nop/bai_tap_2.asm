// Viết chương trình nhập số nguyên n. Kiểm tra n có là số nguyên hoàn thiện hay không ?
.extern printf
.extern scanf

.section .data
    msg_info:        .asciz "Nhập số nguyên n: "
    msg_not_perfect: .asciz "Số %ld không phải là số hoàn thiện.\n"
    msg_perfect:     .asciz "Số %ld là số hoàn thiện.\n"
    msg_integer:     .asciz "%ld"
    num:             .dword 0

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
    b.le not_perfect

    mov x10, #1
    mov x11, #0
	
loop_start:
    lsl x12, x10, #1
    cmp x12, x9
    b.gt loop_end
	
    udiv x12, x9, x10
    mul x12, x12, x10
    sub x12, x9, x12
    cbnz x12, loop_increase
	
    add x11, x11, x10

loop_increase:	
    add x10, x10, #1
    b loop_start
	
loop_end:
    cmp x9, x11
    b.eq perfect

not_perfect:
    adrp x0, msg_not_perfect
    add x0, x0, :lo12:msg_not_perfect
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
    b end
	
perfect:
    adrp x0, msg_perfect
    add x0, x0, :lo12:msg_perfect
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
	
end:
    mov x0, #0
    mov x8, #93
    svc #0
