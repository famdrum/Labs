#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
	char word[25];
	gets(word);
	int check = 0;
	for (int i = 0; i < strlen(word); i++){
		if (word[i] == ' '){
			check = 0;
		} else {
			check++;
		}
		if (check == 1){
			printf("%c", toupper(word[i]));
		}
	}
}