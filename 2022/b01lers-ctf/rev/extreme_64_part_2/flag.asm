SECTION .text
global _start
_start:
  xor rbx, rbx;
loop:
  cmp rbx, 0x20;
  jge print;
  xor rax, rax;
  mov al, [rsi+rbx];
  xor al, 0x82;
  mov [rsi+rbx], al;
  inc rbx;
  jmp loop;
print:
  xor rax, rax;
  mov al, 0x1;
  mov rdi, 0x1;
  mov rdx, 0x20;
  syscall;

