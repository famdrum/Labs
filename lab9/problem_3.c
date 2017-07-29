#include <stdio.h>
#include <stdlib.h>

int main(){
	int n, m;
	scanf("%d", &n);
	scanf("%d", &m);
	int **main = (int**) malloc(sizeof(int) * n);
	for(int i = 0; i < n; i++){
		main[i] = (int*) malloc(sizeof(int) * m); 
	}
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			scanf("%d", *(main + i) + j);
		}
	}
	int v1, v2;
	scanf("%d", &v1);
	scanf("%d", &v2);
	if(v1 > n || v2 > m){
		printf("Wrong numbers!");
		return 1;
	}
	int end = 0;
	for(int i = 0; i < m; i++){
		end = end + *(*(main + v1) + i);
	}
	for(int i = 0; i < n; i++){
		if (i != v1){
			end = end + *(*(main + i) + v2);
		}
	}
	printf("%d", end);
	return 0;
}