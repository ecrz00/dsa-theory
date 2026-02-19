# Sorting algorithms
Searching in an **unsorted array** takes  **O(n)** times,he worst case, the algorithm must iterate through every element (Linear Search). In a sorted array, the same operation takes **O(log n)** using an Algorithm called [**Binary Search**](BinarySeach.md). This approach repeatedly divides the search interval in half, significantly reducing the number of comparisons.

A collection of elements can be arranged in a specific order, (e.g., numbers in ascending/descending order or strings in alophabetic order). Sorting algorithms are generally categorized by their time complexity.

* **Cuadratic O($n^2$)**: There are intuitive and easy to implement, but become significantly slower as the input increases. They are typically only recommended for small datasets or educational purposes.
    * Selection Sort
    * Bubble Sort
    * Insertion Sort
* **Log-linear O($n \log(n)$)**: These utilize a Divide and Conquer strategy, often through recursion, to achieve much higher efficiency. They are the standard for production-level applications dealing with large amounts of data.
    * Merge Sort
    * Quick Sort

## Selection Sort
This algorithm works by repeatedly finding the minimum element from the unsorted part of the data. While the core logic remains the same, it can be implemented in two ways:
* Creating a new array in which all the elements will be copied in order. Given an array ```a = [2, 7, 4, 1]``` and an empty array ```b = []```, the algorithm is executed in a loop: 
    1. Search the minimum element in *a*
    2. Append that element in *b*
    3. Overwrite that element with a big enough value, to avoid picking it again. For example ```a[3] = float('inf')```
<p align="center">
  <img src="../assets/arrays/selectionSort1.gif" width="500" alt="Descripción de la imagen">
  <br>
  <em>Figure 1: Selection sort with extra space.</em>
</p>

```python
def selectionSort(a: list[int]) -> list[int]:
    b = []
    n = len(a)
    for x in range(n): #iterate n times -> O(n)
        minn = float('inf')
        idx = 0
        for i, num in enumerate(a): #iterate n times -> O(n)
            if num < minn:
                minn = num
                idx = i
        b.append(minn)
        a[idx] = float('inf')
    return b
```

* Sorting the collection within the original memory block. It conceptually divides the array into a sorted and an unsorted section. Given an array ```a = [2, 7, 4, 1]``` which will be iterated using *i*: 
    * Search the array for the minimum value.
    * Swap that minimum value with the element at the i-th index.

<p align="center">
  <img src="../assets/arrays/selectionSort2.gif" width="200" alt="Descripción de la imagen">
  <br>
  <em>Figure 2: Selection sort in-place.</em>
</p>

```python
def selectionSort(a: list[int]) -> None:
    n = len(a)
    for i in range(n):
        imin = i
        for j in range(i+1,n):
            if a[j] < a[imin]:
                imin=j
        a[i], a[imin] = a[imin], a[i]

```

Both implementations share the same time complexity, but they differ significantly in how they handle memory:
* **Time Complexity (O($n^2$)):** Both methods take quadratic time because the array is traversed entirely n times (where n is the number of elements). Even if the minimum is found in one step, the scanning must continue.
* **Space Complexity:**
    * Out-of-Place requires **O(n)** space because it allocates a new array of the same size as the original.
    * In-Place requires **O(1)** constant space because it reuses the original memory block and only needs a single temporaty variable for the swap.

## Bubble sort

Bubble sort is an iterative algorithm that "bubbles up" the largest elements to the end of the array by comparing and swapping adjacent neighbors.
* Compare element at i-th with i+1-th position.
* If element at i-th position is bigger, swap them.
    * If at least one swap occurs during a full pass, the array is not yet sorted; the process must repeat.
    * If the algorithm traverses the entire array without a single swap, it means the collection is already sorted, and the execution stops immediately.
* Through each iteration, the bigger elements is pushed to the end, so the range of iteration is reduces.
<p align="center">
  <img src="../assets/arrays/bubbleSort.gif" width="200" alt="Descripción de la imagen">
  <br>
  <em>Figure 3: Bubble Sort.</em>
</p>

```python
def bubbleSort(a: list[int]):
    n = len(a)
    for k in range(n):
        flag = True
        for i in range(n-k-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                flag = False
        if flag:
            break
```

This implementation takes **O($n^2$)** times to run because the array is traversed in a double-nested loop. Even though the inner loop gets shorter with each pass. In Big O analysis, as *n* tends to infinity, subtractions are ignored. 

In termns of space, it occupies constant time **O(1)** because the array is modified in-place.