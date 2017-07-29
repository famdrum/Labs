#include <stdio.h>
#include <stdlib.h>

int main() {
	char arr[10][10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	int a;
	int b;
	scanf("%d", &a);
	scanf("%d", &b);
	if (a < 10 && b < 10 && a > 0 && b > 0) {
		printf(arr[a - 1]);
		printf("\n");
		printf(arr[b - 1]);
		printf("\n");
	} else {
		if (a % 2 == 0){
			printf("odd");
			printf("\n");
		} else {
			printf("even");
			printf("\n");
		}
		if (b % 2 == 0){
			printf("odd");
			printf("\n");
		} else {
			printf("even");
			printf("\n");
		}
	}
}