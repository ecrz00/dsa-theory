'''
Given an array nums (sorted in ascending order) possibly to be rotated, and an integer target, return the index of target if it is in nums, or -1 if it is not.

Approach: Use binary search to find the target. For the seek of simplicity, nums will be a and target will be x there will be 3 cases:
- Case 1: a[mid] == x:     #we have found the target! 
            return mid
- Case 2: a[mid] <= a[high]:    #right-half sorted
    - Case 2.1: x > a[low] and x <= a[high]  #target is between mid-th and high-th index, so we move the low pointer
                    low = mid+1
    - Case 2.2: high = mid-1  #move the high pointer
- Case 3: a[low] <= a[mid]: #left-half sorted
    - Case 3.1: x >= a[low] and x < a[mid] #target is between low-th and mid-th index, so we move the high pointer
                hi=mid-1
    - Case 3.2: low = mid + 1 
'''
def search(nums: list[int], target: int) -> int: #T: O(nlogn), S: O(1)
        lo, hi = 0,len(nums)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<=nums[hi]:
                if target > nums[mid] and target<=nums[hi]:
                    lo=mid+1
                else: hi=mid-1
            elif nums[lo] <= nums[mid]:
                if target >= nums[lo] and target<nums[mid]:
                    hi=mid-1
                else: lo = mid+1
        return -1 