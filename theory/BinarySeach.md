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

BS is commonly utilized to:
* Find first or last occurence of a specific value within a collection.
* Determine the frequency of an element (i.e., how many times an element occurs).
* Identify the rotation count of a sorted array (specifically, how many times an array has been rotated).
* Locate an element within a circularly sorted array.

## First/Last occurence
Given a sorted array ```a = [1,2,3,4,4,4,5,6,7]``` where 4 is the target value, what index should the algorithm return? 
* To find the first occurrence, the search must be continued on the left side, even after the target is initially located. This ensures that any potential matches at lower indices are identified.

```python
def findFirst(arr: list, target:int) -> int:
    n = len(arr)
    res = -1
    lo, hi = 0, n-1
    while lo<=hi:
        mid=lo+((hi-lo)//2)
        if arr[mid] == target:
            res = mid
            hi=mid-1
        elif target<arr[mid]: hi = mid - 1
        else: lo = mid+1
    return res
```

* To find the last occurrence, the search must be continued on the right side even after the target is initially located.

```python
def findLast(arr: list, target: int) -> int:
    n=len(arr)
    lo, hi = 0, n-1
    res=-1
    while lo<=hi:
        mid = lo+((hi-lo)//2)
        if arr[mid] == target:
            res=mid
            lo=mid+1
        elif target < arr[mid]: hi=mid-1
        else: lo = mid+1
    return res 
```

> [!NOTE]
>  A different condition for the while loop is utilized in both implementations. The "inclusive" condition is preferred as it allows the search space to be fully exhausted.

A particular solution to determine the frequency of an element is provided by using the indices of the first and last occurence. So, both functions are called and the returning index are stored. The frequency is then calculated by finding the difference between these two values.

```python
a = [1,2,3,4,4,4,5,6,7]
first = findFirst(a, 4)
last = findLast(a,4)
#the freq is given by last - first + 1 but when the targer is not found, this formula returns a 1 when it should be a 0. So, that special case is handle with the if/else
if first == -1: 
    freq = 0
else:
    freq = last - first + 1
```