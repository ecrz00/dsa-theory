'''
Approach: Counting Sort
Since there are just 3 different colors, we can define an array that will store/represent the occurrences of each color. Then we will
overwrite the original array using slicing based on those counts.
'''
def sortColors(nums: list[int]) -> None:
        count = [0,0,0]
        for color in nums:
            count[color]+=1
        r,w,b = count
        nums[:r]=[0]*r
        nums[r:r+w]=[1]*w
        nums[r+w:]=[2]*b