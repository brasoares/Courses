#include <stdio.h>
//This code requests 3 numbers and tells which is the highest (using nested if statements). 
int main (){
	int a, b, c;
	printf("Enter the first number: \n");
	scanf("%d", &a);
	printf("Enter the second number: \n");
	scanf("%d", &b);
	printf("Enter the third number: \n");
	scanf("%d", &c);
	
	if (a > b && a > c) {
		printf("The first number, %d, is the higher.", a);
	}
	else if (b > a && b > c) {
		printf("The second number, %d, is the higher.", b);
	}
	else{
		printf("The higher entered number is: %d.", c);
	}
}
/* Next:
1: make it check if the numbers are equal and present a message informing there's no higher number.
2: make sure it can work with negative integers: already, by default.
3: use floating point numbers.
4: use double type.
*/
