int main () {
  int num = 999;
  int *ptr; // Pointer declaration
  ptr = &num; // Pointer initialization

  printf("Value of num: %d\n", num);
  printf("Address of num: %p\n", (void *)&num);
  printf("Value of num using pointer: %d\n", *ptr); // Dereferencing pointer
  printf("Address stored in pointer: %p\n", (void *)ptr);

  return 0;
}

/* Example results:

Value of num: 999
Address of num: 0x7ffdb40cc13c
Value of num using pointer: 999
Address stored in pointer: 0x7ffdb40cc13c

As per run on: https://ide.geeksforgeeks.org/online-c-compiler

*/
