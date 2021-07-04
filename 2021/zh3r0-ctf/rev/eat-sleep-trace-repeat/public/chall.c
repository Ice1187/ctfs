#include <stdio.h>

#define STDIN  0
#define STDOUT 1

// STRINGS
char prompt[] = "enter password: ";
char end_prompt[] = "search complete\n";

// 0x402000
unsigned long long magic;
// 0x402008
unsigned long long magics[0x800];
// 0x402808
char in[0x64];
// 0x40286c
char buf3[0x64];

// 0x401005
void input() {
	read(STDIN, in, 0x64);
}

// 0x40105f
void get_magic(unsigned long long num) {
	magic = num;
}

unsigned long long shr(unsigned long long n, int s) {
	for(int i =0; i < s; i++)
		n = n / 2;
	return n;
}

// 0x401023
unsigned long long do_magic() {
	unsigned long long rcx, rdx, rax;
	rcx = magic;
	rdx = rcx;
	rdx = shr(rdx, 0xc); // 12  // get left 4 bits
	rcx = rcx ^ rdx;
	rdx = rcx;
	rdx = rdx << 0x19; // 25
	rcx = rcx ^ rdx;
	rdx = rcx;
	rdx = shr(rdx, 0x1b); // 27
	rcx = rcx ^ rdx;
	rax = rcx * 0x2545f4914f6cdd1d;
	magic = rcx;
	// printf("0x%016llX\n", rax);
	printf("%c\n", (char)rax);
	// printf("%c\n", (char)magic);
	return rax;
}

// 0x401106
int func4(char c) {
	int i = 0;
	while (1) {
		char al = (char)magics[i];
		i++;
		if (i == 0x7ff)
			exit(1);
		else if (al != c)
			continue;
		else 
			return --i;
	}
}

// 0x401068
int main() {
	write(STDOUT, prompt, 16);
	input();
	// func2(0x41424344)
	magic = 0x41424344;   // "ABCD"

	for(int i = 0; i < 0x800; i++) 
		magics[i] = do_magic();

	for (int i = 0; i < 0x64; i++) {
			char ret = func4(in[i]);  // func4(in[i], 0)
			if( ret == -1) {
				return 0;
			}
			buf3[i] = ret;
			// printf("%s\n", buf3);
	}

	write(STDOUT, end_prompt, 16);

	exit(0);
	return 0;
}

