#include <stdio.h> 

int main(){
	char choice;
	int a, b;
	
	printf("Type an integer: \n");
	scanf("%d", &a);
	printf("Type a second one: \n");
	scanf("%d", &b);
	
	printf("Now, consider the first num as 'a' and the second as 'b'.\n");
	printf("In order, which is the operation you wish to perform?\n");
	printf("Please, choose: '+' '-' '*' or '/': (type)\n");
	scanf(" %c", &choice);
	
	switch(choice){
		case '+':
			printf("The result is: %d.\n", a + b);
			break;
		case '-':
			printf("The result is: %d.\n", a - b);
			break;
		case '*':
			printf("The result is: %d.\n", a * b);
			break;
		case '/':
			printf("The result is: %d.\n", a / b);
			break;
		default:
			printf("Not a valid operation.\n");
	}
}
