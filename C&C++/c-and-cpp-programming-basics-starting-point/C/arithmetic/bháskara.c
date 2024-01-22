 #include <stdio.h>
 #include <math.h>
 
 /* Test cases:
 a = 1; b = (2) and c = (3) then delta == 0 
 a = 1; b = (-4) and c = (4) then delta < 0
 a = 2; b = (-5) and c = (-3) then delta > 0
 */
 
 int main (){
 	//variables declaration
 	float a = 0, b = 0, c = 0;
 	float x1 = 0, x2 = 0, delta = 0;
 	
 	printf("Enter variable a: \n");
 	scanf("%f", &a);
 	printf("Enter variable b: \n");
 	scanf("%f", &b);
 	printf("Enter variable c: \n");
 	scanf("%f", &c);
 	
 	if (a != 0){
	
		delta = (pow(b, 2))-(4*(a*c));	
		
		if (delta < 0) {
			printf("There's not a real root, so, x1 = 0 and x2 = 0");
		}
		else if (delta == 0) {
			delta = (x1 = x2 = ((-b)+sqrt(delta))/(2*a));
			printf("Result: %.2f.\n", x1);
		}
		//if delta higher than 0
		else {
			x1 = ((-b)+sqrt(delta))/(2*a);
			x2 = ((-b)-sqrt(delta))/(2*a);
			printf("Results are: x1 = %.2f and x2 = %.2f.\n", x1, x2);
		}
	}
	else {
		printf("Variable a (angular coefficient) must be other than 0.\n");
	}
 }
