'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    -For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
    -For example, the next permutation of [1,2,3] is [1,3,2].
    -Similarly, the next permutation of [2,3,1] is [3,1,2].
    -While the next permutation of [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

Approach:
We are looking for the next permutation, which means: a bigger than the current, but the smallest of the greater ones. Given the list:
[3,4,5] -> [3,5,4] -> [4,3,5] -> [4,5,3] -> [5,3,4] -> [5,4,3]
   ^                                                      ^  
   |                                                      |         
minimum                                                 maximum

If all the elements are sorted in decreasing order (from left to right),then that permutation is the maximum/greater of the bunch, so we need to go back to the first one (where the elements are sorted in increasing order).
On the other hand, from right to left the nums are sorted in increasing order. Then, if we find a number, from right to left, in which the increasing order ends, a next permutation exists. 
    [1,2,5,4,3], idx = 1
       ^
       |
That number will be the pivot: 
- To its right all the numbers are in its maximum possible order ([5,4,3]), so we cannot get a greater permutation. 
- To its left, there are some space to make changes.
The next step is to find the first value greater than the pivot and swap them to each other. Thus, it is ensured the permutation increases.
Finally, we invert the right-side of the list. If the pivot doesn't exist, then the whole list in inverted. 
'''
def nextPermutation(nums: list[int]) -> None: #T: O(n), S: O(1)
    n=len(nums)
    idx=n-2
    while idx>=0 and nums[idx] >= nums[idx+1]: idx-=1
    if idx>=0:
        j=n-1
        while nums[j] <= nums[idx]: j-=1
        nums[idx], nums[j] = nums[j], nums[idx]
    lo, hi = idx+1, n-1
    while lo<hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo+=1
        hi-=1