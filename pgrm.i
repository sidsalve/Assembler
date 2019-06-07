section .data
	s dd sym0
	y dd sym1
	str1 db  sym2 ,10,0
	str2 db  sym3 ,0
	msg db  sym4 ,0,102
	q dd sym0
	e dd sym1
	t db  sym7 ,10,0
	o db  sym8 ,0
	sf db  sym9 ,0
section .bss
	str resd 1
section .text
	global main
main:	
	sub R0 sym2
	mov R3 R2
	mov R1 R2
	mov R4 R5
	mul R0
	mov R5 R6
	xor R0 lit10
	xor R0 lit11
	xor R0 sym2
abc:	
	xor R3 R3
	jmp sym13
bcf:	
