section .data
;	s dd 10,20,30,40
;	y dd 50,60,70,80
	str1 db "this is a string",10,0
	str2 db "this another string 10",0
	msg db "hello",0,102
;	q dd 10,20,30,40
;	e dd 50,60,70,80
	t db "abcdef ghijklmn",10,0
	o db "hello sid",0
	sf db "here the output",0
section .bss
	a resb 1
section .text
	global main
main:
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
abc:
	xor ebx,ebx
	jz bcf
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
	jz abc
bcf:
