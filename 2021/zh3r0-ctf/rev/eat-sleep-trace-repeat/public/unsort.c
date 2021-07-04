#include <stdio.h>

#define STDIN 0
#define STDOUT 1

char enter[] = "enter password: ";
char compl[] = "search complete\n";

unsigned long long magic;
char _buf_0x402008[0x800];
char _buf_402808[0x64];
char _buf_40286c[0x64];

void _401005() {
	read(STDIN, _buf_402808, 0x64);
}

void _40105f(unsigned long long num) {
	magic = num; 
}

unsigned long long _0x401023() {
	unsigned long long rcx, rdx, rax;
	rcx = magic;
	rdx = rcx;
	rdx = rdx / 0x1000;
	rcx = rcx ^ rdx;
	rdx = rcx;
	rdx = rdx << 0x19;
	rcx = rcx ^ rdx;
	rdx = rcx;
	rdx = rdx / 0x8000000;
   	rcx = rcx ^ rdx;
	rax = 0x2545f4914f6cdd1d;
	rax = rax * rcx;
	magic = rcx;
	return rax;
}

unsigned long long _401106(char bl) {
	unsigned long long rdx = 0;
loop: ;
	char al = (char)_buf_0x402008[rdx];
	rdx++;
	if (rdx == 0x7ff)
		goto *0x401131;
	if (al != bl) 
			goto loop;
	rdx--;
	return rdx;
}

int main() {
	write(STDOUT, enter, 0x10);
	_401005();
	_40105f(0x41424344);
	for(int i=0,ecx = 0x800; ecx != 0; i++,ecx--)
		_buf_0x402008[i] = (char)(_0x401023());

	 // printf("%s\n", _buf_0x402008);
	
	for(int i = 0; i < 0x64; i++) { 
		char ret = _401106((char)_buf_402808[i]);	
		if(ret == -1)
			goto *0x4010fa;
		_buf_40286c[i] = (char)ret;
		// printf("%u\n", ret);
	}

	write(STDOUT, compl, 0x10);
	return 0;
}

