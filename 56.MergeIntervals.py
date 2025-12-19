'''
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Approach: The easiest way to solve the problem is create a new array called merged to store the valid intervals. We will traverse the intervals array, at each iteration we append the interval in merged if
it doesn't overlaps with the last element of merged, otherwise we modify the end of the interval if needed.
'''
def merge(intervals: list[list[int]]) -> list[list[int]]: #T: O(nlogn) S: O(n)
    intervals.sort(key = lambda intv: intv[0]) #O(nlogn)
    merged = []
    for inter in intervals:#O(n)
        if not merged or merged[-1][1]<inter[0]:
            merged.append(inter)
        else:
            merged[-1][1] = max(merged[-1][1], inter[1])
    return merged