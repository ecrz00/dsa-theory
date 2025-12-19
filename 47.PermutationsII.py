'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Approach: We are going to use backtrack to compute all the possible permutations. Since the array nums may have duplicates, a dictionary is a
good way to store each number along with its frequency. Instead of traversing the array itself, we will traverse the keys on the dictionary. 
If the frequency of that number is greater than 0 we will consider it and subtract 1 from its frequency, once we backtrack the choice we 
add 1 back.
'''
def permuteUnique(nums: list[int]) -> list[list[int]]: #T: O(n*n!), S: O(n)
    dic = {}
    n=len(nums)
    res, sol = [],[]
    for num in nums:
        dic[num] = dic.get(num,0)+1
    def backtrack():
        if len(sol) == n:
            res.append(sol[:])
            return
        for key in dic.keys():
            if dic[key] > 0:
                sol.append(key)
                dic[key] -= 1
                backtrack()
                tmp = sol.pop()
                dic[tmp] += 1
    backtrack()
    return res