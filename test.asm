section .data
	str1 db "this is string",10,0
	len1 equ $ - str1
section .text
	global main
main:
	mov eax,1
	mov ebx,4
abc:	mov ecx,str1
	mov edx,len1
	int 80h
	loop abc
	
