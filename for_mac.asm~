%macro write 2
	mov eax,1
	mov ebx,4
	mov ecx,%1
	mov edx,%2
	int 80h
%endmacro
%macro read 2
	mov eax,1
	mov ebx,4
	mov ecx,%1
	mov edx,%2
	int 80h
%endmacro
section .data
	str1 db "good",10,0
	len1 equ $ - str1
	msg db "file",0,102
	len2 equ $ - msg
section .text
	global main
main:
	write str1,len1
	write msg,len2
	add ebx,ecx
	read str1,len1
	mov eax,ebx
	mov ecx,edx
	add eax,ebx
	xor eax,eax
