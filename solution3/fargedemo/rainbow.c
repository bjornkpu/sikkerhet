#include <stdio.h>
#include "fargeskrift.h"

void rainbow() {

  int roggbif[8] = {1, 3, 2, 6, 4, 5, 7,0};

  for (int i = 0; i < 8; i++) {
    farge_printf(7, roggbif[i], "   ");
  }
}


int main(int argc, char *argv[]) {
	rainbow();
}
