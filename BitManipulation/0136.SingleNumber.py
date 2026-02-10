'''
Approach:
The solution takes advantage of an XOR property: any number XORed with itself is 0. Since all numbers except one appear twice, applying XOR to the entire array cancels out the pairs and the remaining result is the one that appears only once.

Complexity:
- Time: O(n) -> One single pass through the list.
- Space: O(1) -> We only use one integer variable.
'''
def singleNumber(nums: list[int]) -> int:
    carry = 0
    for num in nums:
        carry ^= num
    return carry