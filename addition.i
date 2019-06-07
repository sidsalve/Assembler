section .data
	a dd sym0
	b dd sym1
	msg db  sym2 ,10,0
section .text
	global main
	extern printf scanf
main:	
	mov R0 dword[sym0]
	mov R2 dword[sym1]
	mov R0 R3
	add R0 R2
	push R0
	push sym2
	call printf
	add R4 lit3
