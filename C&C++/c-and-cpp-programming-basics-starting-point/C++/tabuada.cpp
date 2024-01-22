#include <stdio.h>

int main () {
	int factor, i;
	
	i = 0;
	
	printf("Which multiplication table?\n");
	scanf("%d", &factor);
	
	while (i <= 10){
		printf("%d x %d = %d\n", factor, i, (i*factor));
		i++;
	}
}
