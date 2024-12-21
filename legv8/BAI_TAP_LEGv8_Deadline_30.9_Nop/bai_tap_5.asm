// Viết chương trình thực hiện các chức năng sau:
//		Nhập mảng 1 chiều n phần tử số nguyên
//		Xuất mảng
//		Liệt kê các số nguyên tố
//		Tìm giá trị lớn nhất trong mảng
//		Tính trung bình mảng
.extern printf
.extern scanf

.section .data
    msg_import_info:    .asciz "Nhập số lượng phần tử: "
    msg_import_item:    .asciz "Nhập a[%ld]: "
    msg_export_info:    .asciz "Mảng đã nhập:\n"
    msg_export_item:     .asciz "   a[%ld] = %ld\n"
    msg_primes_info:     .asciz "Các số nguyên tố trong mảng:\n"
    msg_maximum_info:    .asciz "Giá trị lớn nhất: %d\n"
    msg_average_info:    .asciz "Giá trị trung bình: %d\n"
    msg_integer:         .asciz "%ld"
    size:                .dword 0

.section .bss
    arr:    .space 1024
    stack:  .space 1024

.section .text

.global main
.global _array_import
.global _array_export
.global _array_list_primes
.global _array_find_max
.global _array_average

main:    
    adrp x1, stack
    add x1, x1, :lo12:stack
    add x1, x1, 4096
    mov sp, x1
    
    bl _array_import
    bl _array_export
    bl _array_list_primes
    bl _array_find_max
    bl _array_average

    mov x0, #0
    mov x8, #93
    svc #0

_array_import:
    sub sp, sp, #8
    str x30, [sp]
    sub sp, sp, #8
    str x19, [sp]
    sub sp, sp, #8
    str x20, [sp]
    sub sp, sp, #8
    str x21, [sp]

    adrp x0, msg_import_info
    add x0, x0, :lo12:msg_import_info
    bl printf

    adrp x0, msg_integer
    add x0, x0, :lo12:msg_integer
    adrp x1, size
    add x1, x1, :lo12:size
    bl scanf

    adrp x19, arr
    add x19, x19, :lo12:arr
    adrp x20, size
    add x20, x20, :lo12:size
    ldr x20, [x20]
    mov x21, #0

array_import_loop:
    cmp x21, x20
    b.ge array_import_end
    
    adrp x0, msg_import_item
    add x0, x0, :lo12:msg_import_item
    mov x1, x21
    bl printf

    adrp x0, msg_integer
    add x0, x0, :lo12:msg_integer
    mov x1, x19
    bl scanf
    
    add x19, x19, #8
    add x21, x21, #1
    b array_import_loop
    
array_import_end:
    ldr x21, [sp]
    add sp, sp, #8
    ldr x20, [sp]
    add sp, sp, #8
    ldr x19, [sp]
    add sp, sp, #8
    ldr x30, [sp]
    add sp, sp, #8
    ret    

_array_export:
    sub sp, sp, #8
    str x30, [sp]
    sub sp, sp, #8
    str x19, [sp]
    sub sp, sp, #8
    str x20, [sp]
    sub sp, sp, #8
    str x21, [sp]

    adrp x0, msg_export_info
    add x0, x0, :lo12:msg_export_info
    bl printf

    adrp x19, arr
    add x19, x19, :lo12:arr
    adrp x20, size
    add x20, x20, :lo12:size
    ldr x20, [x20]
    mov x21, #0

array_export_loop:
    cmp x21, x20
    b.ge array_export_end

    adrp x0, msg_export_item
    add x0, x0, :lo12:msg_export_item
    mov x1, x21
    ldr x2, [x19]
    bl printf

    add x19, x19, #8
    add x21, x21, #1
    b array_export_loop
    
array_export_end:
    ldr x21, [sp]
    add sp, sp, #8
    ldr x20, [sp]
    add sp, sp, #8
    ldr x19, [sp]
    add sp, sp, #8
    ldr x30, [sp]
    add sp, sp, #8
    ret    

_array_list_primes:
    sub sp, sp, #8
    str x30, [sp]
    sub sp, sp, #8
    str x19, [sp]
    sub sp, sp, #8
    str x20, [sp]
    sub sp, sp, #8
    str x21, [sp]
    sub sp, sp, #8
    str x22, [sp]
    sub sp, sp, #8
    str x23, [sp]

    adrp x0, msg_primes_info
    add x0, x0, :lo12:msg_primes_info
    bl printf

    adrp x19, arr
    add x19, x19, :lo12:arr
    adrp x20, size
    add x20, x20, :lo12:size
    ldr x20, [x20]
    mov x21, #0

array_list_primes_loop:
    cmp x21, x20
    b.ge array_list_primes_end

    ldr x22, [x19]
    cmp x22, #1
    b.le not_prime

    cmp x22, #3
    b.le prime

    mov x23, #2

check_prime_loop:
    lsl x9, x23, #1
    cmp x9, x22
    b.gt prime

    udiv x10, x22, x23
    mul x10, x10, x23
    sub x10, x22, x10
    cbz x10, not_prime

    add x23, x23, #1
    b check_prime_loop

prime:
    adrp x0, msg_export_item
    add x0, x0, :lo12:msg_export_item
    mov x1, x21
    ldr x2, [x19]
    bl printf

not_prime:    
    add x19, x19, #8
    add x21, x21, #1
    b array_list_primes_loop
    
array_list_primes_end:
    ldr x23, [sp]
    add sp, sp, #8
    ldr x22, [sp]
    add sp, sp, #8
    ldr x21, [sp]
    add sp, sp, #8
    ldr x20, [sp]
    add sp, sp, #8
    ldr x19, [sp]
    add sp, sp, #8
    ldr x30, [sp]
    add sp, sp, #8
    ret    

_array_find_max:
    sub sp, sp, #8
    str x30, [sp]
    sub sp, sp, #8
    str x19, [sp]
    sub sp, sp, #8
    str x20, [sp]
    sub sp, sp, #8
    str x21, [sp]
    sub sp, sp, #8
    str x22, [sp]
    sub sp, sp, #8
    str x23, [sp]

    adrp x19, arr
    add x19, x19, :lo12:arr
    adrp x20, size
    add x20, x20, :lo12:size
    ldr x20, [x20]
    mov x21, #0
    ldr x22, [x19]
    mov x23, #0

array_find_max_loop:
    cmp x21, x20
    b.ge array_find_max_end

    ldr x9, [x19]
    cmp x9, x22
    b.le not_max

    mov x22, x9
    mov x23, x21

not_max:
    add x19, x19, #8
    add x21, x21, #1
    b array_find_max_loop
    
array_find_max_end:
    adrp x0, msg_maximum_info
    add x0, x0, :lo12:msg_maximum_info
    mov x1, x22
    bl printf

    ldr x23, [sp]
    add sp, sp, #8
    ldr x22, [sp]
    add sp, sp, #8
    ldr x21, [sp]
    add sp, sp, #8
    ldr x20, [sp]
    add sp, sp, #8
    ldr x19, [sp]
	add sp, sp, #8
	ldr x30, [sp]
	add sp, sp, #8
	ret

_array_average:
	sub sp, sp, #8
	str x30, [sp]
	sub sp, sp, #8
	str x19, [sp]
	sub sp, sp, #8
	str x20, [sp]
	sub sp, sp, #8
	str x21, [sp]
	sub sp, sp, #8
	str x22, [sp]

	adrp x19, arr
	add x19, x19, :lo12:arr
	adrp x20, size
	add x20, x20, :lo12:size
	ldr x20, [x20]
	mov x21, #0
	mov x22, #0

array_average_loop:
	cmp x21, x20
	b.ge array_average_end

	ldr x9, [x19]
	add x22, x22, x9

	add x19, x19, #8
	add x21, x21, #1
	b array_average_loop

array_average_end:
	udiv x22, x22, x20

	adrp x0, msg_average_info
	add x0, x0, :lo12:msg_average_info
	mov x1, x22
	bl printf

	ldr x22, [sp]
	add sp, sp, #8
	ldr x21, [sp]
	add sp, sp, #8
	ldr x20, [sp]
	add sp, sp, #8
	ldr x19, [sp]
	add sp, sp, #8
	ldr x30, [sp]
	add sp, sp, #8
	ret