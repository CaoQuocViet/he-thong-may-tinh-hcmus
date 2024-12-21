// Viêt chương trình nhập số nguyên n. Kiểm tra n có phải là số nguyên tố hay không ?
.extern printf
.extern scanf

.section .data
    msg_info:        .asciz "Nhập số nguyên n: "
    msg_not_prime:   .asciz "Số %ld không phải là số nguyên tố.\n"
    msg_prime:       .asciz "Số %ld là số nguyên tố.\n"
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
    b.le not_prime
	
    cmp x9, #3
    b.le prime
	
    mov x10, #2
	
loop_start:
    lsl x11, x10, #1
    cmp x11, x9
    b.gt prime
	
    udiv x11, x9, x10
    mul x11, x11, x10
    sub x11, x9, x11
    cbz x11, not_prime
	
    add x10, x10, #1
    b loop_start
	
prime:
    adrp x0, msg_prime
    add x0, x0, :lo12:msg_prime
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
    b end
	
not_prime:
    adrp x0, msg_not_prime
    add x0, x0, :lo12:msg_not_prime
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf

end:
    mov x0, #0
    mov x8, #93
    svc #0