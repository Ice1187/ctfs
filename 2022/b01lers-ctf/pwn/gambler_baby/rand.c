#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char s[8] = {0};

  for (int round = 0; round < (1000 - 100) / 10; round++) {
    for (int i = 0; i < 4; i++)
      s[i] = rand() % 26 + 97;

    printf("%s\n", s);
  }

  return 0;
}
