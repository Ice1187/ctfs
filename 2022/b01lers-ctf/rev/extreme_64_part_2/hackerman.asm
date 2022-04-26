SECTION .text
global _start
_start:
  mov rbx, 0x616d72656b636168
  push rbx
  push rsp
  pop rsi
  xor rax, rax
  mov al, 0x1
  mov rdi, 0x1
  mov rdx, 0x8
  syscall
  mov rbx, 0x6e
  push rbx
  push rsp
  pop rsi
  xor rax, rax
  mov al, 0x1
  mov rdi, 0x1
  mov rdx, 0x1
  syscall
