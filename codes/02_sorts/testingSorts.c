#include <stdio.h>
#include "sorts.h"

int main(int argc, const char * argv[]) {
  
  int v1[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v2[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v3[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
 
  int N = 10;
  
  printArray(v1, N);
  
  bubbleSort(v1, N);
  printArray(v1, N);
  
  selectionSort(v2, N);
  printArray(v2, N);
 
  insertionSort(v3, N);
  printArray(v3, N);
 
  return 0;
  
}
