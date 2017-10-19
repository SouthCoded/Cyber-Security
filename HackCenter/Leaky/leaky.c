#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>


char buf[80];

int main (int argc, char **argv)
{

  unsigned int filler0 = 0x71751075;
  unsigned int filler1 = 0x70755011;
  unsigned int filler2 = 0x70757055;
  unsigned int filler3 = 0x10757001;
  unsigned int key = ???;
  unsigned int filler4 = 0x70571007;
  unsigned int filler5 = 0x51107055;
  unsigned int filler6 = 0x50755011;

  unsigned int red = read(STDIN_FILENO,buf,80);
  buf[red] = '\x00';
  printf(buf);
}
