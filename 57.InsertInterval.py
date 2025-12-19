'''
Approach: We are going to implement the same solution used in problem 56. Sort the list and create a new array to store the merged intervals. We will append the newInterval 
into intervals at the beginning. Then everything is the same. 
'''
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]: #T: O(nlogn) S: O(n)
    intervals.append(newInterval)
    intervals.sort(key = lambda inter: inter[0])
    merged = []
    for inter in intervals:
        if not merged or merged[-1][1] < inter[0]:
            merged.append(inter)
        else:
            merged[-1][1] = max(merged[-1][1], inter[1])
    return merged
