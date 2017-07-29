#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char alph[30] = "abcdefghijklmnopqrstuvwxyz";

char ind(char let){
	for (int r = 0; r < strlen(alph); r++){
		if (let == alph[r]){
			return r;
			printf("%s\n", r);
		}
	}
}

int main(int argc, char *argv[]){
	if (argc != 2){
		printf("Try again");
		return 1;
	}
	for (int i = 0; i < argv[1][i] != '\0'; i++){
		if (!isalpha(argv[1][i])){
			printf("Try again");
			return 1;
		}
	}
	char word[100];
	char word1[100];
	int z = 0;
	gets(word);
	strcpy(word1, word);
	if (strlen(argv[1]) > strlen(word)){
		printf("Try again");
		return 1;
	}
	for (int i = 0; i < strlen(word); i++){
		if (isupper(word[i])){
			word1[i] = (((word[i] - 65) + (argv[1][i % strlen(argv[1])] - 97)) % 26) + 65;
		} else {
			word1[i] = (((word[i] - 97) + (argv[1][i % strlen(argv[1])] - 97)) % 26) + 97;
		}
	}
	printf("%s", word1);
	return 0;
}