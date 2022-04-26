from pwn import *

code = b'code{asm_c4n_d0_anything_java_can_do}'

p = remote('ctf.b01lers.com', 9302)

p.recv()
p.recv()
p.recv()
p.sendline(code)

print(p.recv().decode())

asm = b'''xor rbx, rbx;
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
'''
p.sendline(asm)
print(p.recv().decode())
print(p.recv().decode())
print(p.recv().decode())
