#include <stdio.h>

int main() {
    // Declare variables for length, width, and area

    float length = 0;
    float width = 0;
    float area = 0;

    // Prompt the user to enter the length of the rectangle

    printf("Enter the rectangle's length: ");

    // Read the length from the user input

    scanf("%f", &length);

    // Prompt the user to enter the width of the rectangle

    printf("Enter the rectangle's width: ");

    // Read the width from the user input

    scanf("%f", &width);

    // Calculate the area of the rectangle

    area = length * width;

    // Display the result

    printf("%f", area);

    return 0;
}
