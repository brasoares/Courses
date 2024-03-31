include <stdio.h>

char userChoice;

printf("Enter you choice: ");
scanf("%s", &userChoice);

switch(userChoice) {
  case 'a':
    printf("You chose option A.\n");
    break;
  case 'b':
    printf("You chose option B.\n");
    break;
  default:
    printf("Invalid choice.\n");
}
