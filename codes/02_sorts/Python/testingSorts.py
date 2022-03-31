# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

from sorts import *

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
if __name__ == '__main__':

    array = [54,26,93,17,77,31,44,55,20]

    array1 = list(array)
    array2 = list(array)
    array3 = list(array)
    array4 = list(array)
    array5 = list(array)

    print("* BubbleSort: ")
    print("Antes: ", array1)
    bubbleSort(array1)
    print("Depois:", array1)
    print("\n")

    print("* Short BubbleSort: ")
    print("Antes: ", array2)
    shortBubbleSort(array2)
    print("Depois:", array2)
    print("\n")

    print("* SelectionSort: ")
    print("Antes: ", array3)
    selectionSort(array3)
    print("Depois:", array3)
    print("\n")

    print("* InsertionSort: ")
    print("Antes: ", array4)
    insertionSort(array4)
    print("Depois:", array4)
    print("\n")

    print("* MergeSort: ")
    print("Antes: ", array5)
    mergeSort(array5)
    print("Depois:", array5)
    print("\n")

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
