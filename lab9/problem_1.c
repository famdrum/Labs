#include <stdio.h>
#include <stdlib.h>

int* multiply(int* arr, int n) {
    int i;
    int* newArr = (int*) malloc(sizeof(int) * n);
    for (i = 0; i < n; i++) {
        newArr[i] = arr[i] * 2;
    }
    return newArr;
}

int* parse(int* arr, int n){
	int j = 0;
	for(int i = 0; i < n; i++){
		if(arr[i] >= 0){
			j++;
		}
	}
	int* newArr = (int*) malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++){
		if(arr[i] >= 0){
			newArr[i] = arr[i];
			printf("%d\n", newArr[i]);
		}
	}
	return newArr;
}

int main() {
    int n;
    scanf("%d", &n);
    int* arr;
    arr = (int*) malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("\n");
    
    int* arrNew = multiply(arr, n);
    
    for (int i = 0; i < n; i++) {
        if (i != n - 1) {
            printf("%d ", arrNew[i]);
        } else {
            printf("%d\n", arrNew[i]);

        }
    }
	int* arrNe = parse(arr, n);
    return 0;
}