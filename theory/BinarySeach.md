# Binary Seach
Given a sorted array of integers ```a = [2, 6, 13, 21, 36, 47, 63, 81, 97]```, there are two different methods of searching for a*target* element:
* **Linear search:** The entire array is traversed from index 0 to n until the target is either found of the end is reach.
    * **Best case:** Only one comparison is required **O(1)**
    * **Worst case:** *n* comparisons are performed **O(n)**
* **Binary seach:** The element at a middle position *mid* is compared with the *target*. Based on this comparison, one of three scenarios occurs:
    * Case 1: The *target* is found at the middle position.
    * Case 2: If the *target* is less than a[mid], all elements to the right are discarded.
    * Case 3: If the *target* is greater than a[mid], all elements to the left are discarded.
    * Exception: If the *target* was not found return -1.

Binary Search, for seek of simplicity called **BS**, uses a two pointers approach, where *low* and *high* variables point to left and right bound respectively. 
* When **Case 2** is met, all elements from *mid* to *high* are greater than *target*, so *high* value is changed to *mid-1*
* When **Case 3** is met, all elements from *low* to *mid* are greater than *target*, so *low* value is changed to *mid+1*

```python
def BinarySeach(arr: list, target: int)-> int:
    n=len(arr)
    low, high = 0, n-1
    while low < high:
        mid = low + ((high - low)//2)
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            high = mid-1
        else:
            low = mid + 1
    return -1
``` 
