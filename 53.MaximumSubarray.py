'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Approach: We will use to variables, one to store the current sum and another to store the maximum sum we have found so far. The idea is simple: determine whether extend the 
summ or start again, for example:
    nums = [-2,1,-3,4,-1,2,1,-5,4], max_sum = -float('inf'), cur_sum = 0
if our cur_sum is greater than 0, we will extend the sum. Otherwise, we reset the cur_sum to the current num of nums.
On each iteration, we will compute the max sum. 
'''
def maxSubArray(nums: list[int]) -> int:
    cur_sum, max_sum = 0, -float('inf')
    for num in nums:
        if cur_sum > 0:
            cur_sum += num
        else:
            cur_sum = num
        max_sum = max(cur_sum, max_sum)
    return max_sum
