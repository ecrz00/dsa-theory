'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in 
order.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Approach: 
We are going to use Binary Search to find the target,
- If it is found during the while loop, just return mid-th index.
- If we could not find it, nums at mid-th index will be the closest to target, so we will return mid if nums[mid]>=target, otherwise we return mid+1  
'''
def searchInsert(nums: list[int], target: int) -> int:
        n=len(nums)
        lo, hi = 0,n-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target: return mid
            elif nums[mid]>target: hi=mid-1
            else: lo+=1
        return mid+1 if nums[mid]<target else mid