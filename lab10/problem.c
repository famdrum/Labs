#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int n;
	printf("Enter number of students: ");
	scanf("%d", &n);
	struct student{
		int id;
		char name[25];
	} student[n], stud;
	printf("Enter names: ");
	for(int i = 0; i <= n; i++){
		student[i].id = i;
		gets(student[i].name);
	}
	for(int l = 1; l <= n; l++){
		for(int i = 0; i <= n - l; i++){
			if(student[i].name[0] > student[i + 1].name[0]){
				stud = student[i];
				student[i] = student[i + 1];
				student[i + 1] = stud;
			}
		}
	}
	if(n % 2 == 0){
		for(int i = 1; i <= n/2; i++){
			printf("%s %s\n", student[i].name, student[(n+1) - i].name);
		}
	}else{
		for(int i = 1; i <= (n+1)/2; i++){
			if(i == (n+1) - i){
				printf("%s teacher\n", student[i].name);
			}else{
				printf("%s %s\n", student[i].name, student[(n+1) - i].name);
			}
		}
	}
}