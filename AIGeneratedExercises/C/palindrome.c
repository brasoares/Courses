#include <stdio.h>
#include <string.h>

int main () {
  char word[18];
  printf("Entre com a palavra: ");
  scanf("%s", word);

  int length = strlen(word);
  char reversed[length + 1];

  for(i = 0; str[i] != '\0'; i++) {
    reversed[i] = word[length - i - 1]
  }
  
  return 0;
}
