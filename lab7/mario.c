#include <stdio.h>
#include <stdlib.h>

int main() {
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 9; j++){
			if (j < 7 - i) {
				printf(" ");
			} else {
				printf("#");
			}
		}
		printf("\n");
	}
}