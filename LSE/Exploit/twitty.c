#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <signal.h>

void maintenance() {
  printf("MAINTENANCE MODE\n");
  fflush(stdout);
  system("/usr/bin/stdbuf -i0 -o0 -e0 /bin/bash");
}

char * prefix = "Twit: ";
char * post(uint8_t * msg, int len) {
  // Super long canaries for extra security
  unsigned long long canary = CANARY;
  char local[128];
  strcpy(local, prefix);
  // No need to worry about overflows since we compile with canaries
  memcpy(local+strlen(prefix), msg, len);
  if (canary != CANARY) {
    puts("Stack smashing detected\n");
    exit(1);
  }
  return strdup(local);
}

void handler(int sig) {

  exit(1);

}

int main(int argc, char ** argv) {
  uint8_t buffer[256];
  signal(SIGALRM, handler);
  alarm(2);
  int len = read(0, buffer, sizeof(buffer));
  char * format = post(buffer, len);
  printf("%s", format);
  fflush(stdout);
  exit(0);
}


// compile with gcc -m32 -fno-stack-protector -o twitty twitty.c
