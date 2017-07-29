#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char argv[]){
	if (argc != 2){
		printf("Try again");
		return 1;
	}
	int k = argv[1];
	if (k){
		char word[100];
		char word1[100]; 
		gets(word);
		char alph[30] = "abcdefghijklmnopqrstuvwxyz";
		for (int i = 0; i<strlen(word) ; i++) {
			word1[i] = word[i];
		}
		int z;
		for (int i = 0; i < strlen(word); i++){
			if (word[i] != ' ' && strchr(alph, tolower(word[i]))){
				for (int r = 0; r < strlen(alph); r++){
					if (tolower(word[i]) == alph[r]){
						z = r;
						break;
					}
				}
				word[i] = alph[(z + k) % strlen(alph)];
			}
		}
		for (int i = 0; i < strlen(word); i++){
			if (word1[i] == toupper(word1[i])){
				word[i] = toupper(word[i]);
			}
		}
		printf("%s", word);
		return 0;
	} else{
		printf("Try again");
		return 1;
	}
}