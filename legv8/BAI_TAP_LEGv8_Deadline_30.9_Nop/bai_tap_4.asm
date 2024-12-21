// Viết chương trình nhập số nguyên n. Kiểm tra n có là số đối xưng hay không ?
.extern printf
.extern sprintf
.extern scanf
.extern sscanf

.section .data
    msg_info:                .asciz "Nhập số nguyên n: "
    msg_not_palindromic:     .asciz "Số %ld không phải là số đối xứng.\n"
    msg_palindromic:         .asciz "Số %ld là số đối xứng.\n"
    msg_integer:             .asciz "%ld"
    num:                     .dword 0
    num_rev:                 .dword 0
	
.section .bss
    arr: .space 64
	
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

    cmp x9, #0
    b.lt not_palindromic
    cmp x9, #10
    b.lt palindromic

    adrp x0, arr
    add x0, x0, :lo12:arr
    adrp x1, msg_integer
    add x1, x1, :lo12:msg_integer
    adrp x2, num
    add x2, x2, :lo12:num
    ldur x2, [x2]
    bl sprintf
	
    mov x9, x0
    sub x9, x9, #1
    adrp x10, arr
    add x10, x10, :lo12:arr		
    mov x11, #0
	
loop_start:
    cmp x11, x9	
    b.gt loop_end
	
    ldrb w12, [x10, x11]
    ldrb w13, [x10, x9]
    strb w13, [x10, x11]
    strb w12, [x10, x9]
    add x11, x11, #1
    sub x9, x9, #1
    b loop_start
	
loop_end:
    adrp x0, arr
    add x0, x0, :lo12:arr
    adrp x1, msg_integer
    add x1, x1, :lo12:msg_integer
    adrp x2, num_rev
    add x2, x2, :lo12:num_rev
    bl sscanf
	
    adrp x9, num
    add x9, x9, :lo12:num
    ldur x9, [x9]
	
    adrp x10, num_rev
    add x10, x10, :lo12:num_rev
    ldur x10, [x10]
	
    cmp x9, x10
    b.eq palindromic
	
not_palindromic:
    adrp x0, msg_not_palindromic
    add x0, x0, :lo12:msg_not_palindromic
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf
    b end

palindromic:
    adrp x0, msg_palindromic
    add x0, x0, :lo12:msg_palindromic
    adrp x1, num
    add x1, x1, :lo12:num
    ldur x1, [x1]
    bl printf

end:
    mov x0, #0
    mov x8, #93
    svc #0
