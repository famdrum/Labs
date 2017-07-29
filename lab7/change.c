#include  <stdio.h>

int main(){
	int arr[4] = {25, 10, 5, 1};
	int ch;
	int count = 0;
	scanf("%d", &ch);
	while(ch != 0){
		while (ch - arr[0] < 0){
			for(int counter = 0; counter < sizeof(*arr) - 1; counter++){
				arr[counter] = arr[counter+1];
			}
		}
		ch = ch - arr[0];
		count++;
	}
	printf("Minimum quantity of coins is: %d", count);
}