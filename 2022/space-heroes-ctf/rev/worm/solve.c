#include "openssl/sha.h"
#include <stdio.h>
#include <stdlib.h>

SHA256_CTX ctx;
unsigned char *out;

void sha256(int x, int y) {
  long long val;

  val = 16 * x + y;
  SHA256_Update(&ctx, &val, 8);
  SHA256_Final(out, &ctx);

  printf("hash: ");
  for (int i = 0; i < 32; i++)
    printf("%02x", out[i]);
  printf("\n");
}

int main(void) {
  int pos, rnd, x, y;
  srand(0x2454);
  SHA256_Init(&ctx);
  out = (unsigned char*) malloc(sizeof(char)*SHA256_DIGEST_LENGTH);

  for (int i = 1; i != 661; i++) {
    rnd = rand() % 33;
    pos = rand() % 20 + 20 * rnd;

    x = pos / 20;
    y = pos % 20;

    printf("pos: %d\n", pos);
    printf("x: %d  y:%d\n", x, y);

    sha256(x, y);
  }

  char flag[32] = {0xB2, 0xEA, 0xE5, 0xBF, 0xBB, 0x8C, 0xC6, 1,
                   0x38, 0x72, 0xB, 0x2F, 0xF, 0x54, 0x9C, 0x6E,
                   0x40, 0x24, 0xEA, 0x84, 0xC7, 0xE1, 0x7D, 0x34,
                   0x58, 0xBD, 0x2E, 0xE2, 0xB4, 0x12, 0x48, 0xFE};
  printf("shctf{");
  for(int i = 0 ; i < 32; i++) {
    flag[i] ^= out[i];
  }
  printf("%.32s}\n", flag);
}
