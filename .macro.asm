section .data
	str1 db "good",10,0
	len1 equ $ - str1
	msg db "file",0,102
	len2 equ $ - msg
section .text
	global main
main:
mov eax,1
	mov ebx,4
	mov ecx,str1
	mov edx,len1
	int 80h
	mov eax,1
	mov ebx,4
	mov ecx,msg
	mov edx,len2
	int 80h
		add ebx,ecx
mov eax,1
	mov ebx,4
	mov ecx,str1
	mov edx,len1
	int 80h
		mov eax,ebx
	mov ecx,edx
	add eax,ebx
	xor eax,eax
