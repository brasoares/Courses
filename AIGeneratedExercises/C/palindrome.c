#include <stdio.h>
#include <string.h>

int main () {
  char word[18];
  printf("Entre com a palavra: ");
  scanf("%s", word);

  int length = strlen(word);
  char reversed[length + 1];

  
  int i;

  for(i = 0; i < length; i++) {
    reversed[i] = word[length - i - 1]

  if reversed == word:
    print
  else:
    print("%s is not a palindrome.\n", word);
  }
  
  return 0;
}
