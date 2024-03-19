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
