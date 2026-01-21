'''
Approach: 
We will use a three pointers approach. We fill nums1 starting from the end to avoid using extra space and prevent overwriting elements in nums1 that haven't been compared 
yet.

Visual Trace: 
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3

Initial state:
nums1: [ 1,  2,  3,  0,  0,  6 ]  <-- (6 > 3, so 6 goes to the end)
                 ^ x         ^ z
nums2: [ 2,  5,  6 ]
                 ^ y

Next steps:
- Compare 3 and 5: 5 is larger -> nums1[z=4] = 5, y--, z--
- Compare 3 and 2: 3 is larger -> nums1[z=3] = 3, x--, z--
- Compare 2 and 2: equal (else) -> nums1[z=2] = 2, y--, z--

Final result: [1, 2, 2, 3, 5, 6]

Complexity:
- Time: O(m + n) -> One single pass through both arrays.
- Space: O(1) -> In-place modification.
'''
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    x,y = m-1,n-1
    for z in range(m+n-1,-1,-1):
        if x<0:
            nums1[z]=nums2[y]
            y-=1
        elif y<0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x-=1
        else:
            nums1[z] = nums2[y]
            y-=1