'''
Approach:
We will use a hashset to lookup in constant time and to identify the start of each possible sequence.

Every number can be the start of a sequence once and only can be part of a sequende once per while cycle, so each element is visit at max 2 times.

nums = [100, 4, 200, 1, 3, 2]
set = {1, 2, 3, 4, 100, 200}

- with 100: 99 in Set? No -> Start counting: 100 -> 101 in Set? No. Count=1.
- with 4: 3 in Set? Yes -> Skip 'cause it's part of a sequence, not the start.
- with 200: 199 in Set? No -> Start counting: 200 -> 201 in Set? No. Count=1.
- with 1: 0 in Set? No -> Start counting: 1, 2, 3, 4 -> 5 in Set? No. Count=4.
- with 3: 2 in Set? Yes -> Skip.
- with 2: 1 in Set? Yes -> Skip.

Max Count: 4

Complexity:
- Time: O(n) -> Each number is visited at most twice.
- Space: O(n) -> To store the set of numbers.
'''
def longestConsecutive(nums: list[int]) -> int:
    sett = set(nums)
    res=0
    for num in sett:
        if num-1 not in sett: #check if this is the start of a sequence
            next_num=num+1
            count=1
            while next_num in sett: #count how long the sequence is
                count+=1
                next_num+=1
            res = max(res, count)
    return res