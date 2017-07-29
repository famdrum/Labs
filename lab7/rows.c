#include <stdio.h>
#include <math.h>

char word[100];
char end[10][10];

int main() {
    char i;
    int count = 0;
    while (scanf("%c", &i) == 1 && i != '\n') {
        if (i != ' ') {
            word[count] = i;
			count++;
        }
    }
    int length = sqrt(count + 1);
    int height = length;
    int a, b;
    while (height * length < count + 1){
		height++;
		length++;
	}
    for (int a = 0; a <= count; a++) {
        end[a / length][a % length] = word[a];
    }
    for (int b = 0; b < length; b++) {
        for (int a = 0; a < height; a++) {
            printf("%c", end[a][b]);
        }
    }
}