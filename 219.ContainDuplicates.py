'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
'''
def containsNearbyDuplicate(nums: list[int], k: int) -> bool: #T: O(n), S: O(n)
    dic = {}
    minn = float('inf')
    for i in range(len(nums)):
        if nums[i] in dic:
            minn = min(minn, abs(dic[nums[i]]-i))
            if minn <= k:
                return True
        dic[nums[i]]=i
    return False