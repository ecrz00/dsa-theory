'''
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Approach: As a first glimpse, the idea is starting at index 0, check all the combinations of jumps to find if there is a way to reach the end of the array. But, we can start
at index n-2 (the next-to-last element) and check whether we can reach the n-1 position, this will be our target. 
With each iteration, if we can reach target with nums[i]+i, then the new target will be i. At the end, if there is a way to reach the last element, target will be 0, 
otherwise it will be any other number. 
'''
def canJump(nums: list[int]) -> bool:
    n=len(nums)
    target = n-1
    for i in range(n-2,-1,-1):
        if nums[i]+i >=target:
            target = i
    return target == 0