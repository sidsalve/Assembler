section .data
	a dd 10
	b dd 20
	msg db "Addition is %d",10,0
section .text
	global main
	extern printf,scanf
	main:
	mov eax,dword[a]
	mov edx,dword[b]
	mov eax,ebx
	add eax,edx
	push eax
	push msg
	call printf
	add esp,8


	mov ebx,dword[a]
	mov ecx,dword[a]
	mov ebx,ecx
	add ebx,8
