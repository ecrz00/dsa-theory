'''
Approach: 
- split(): Removes all leading/trailing whitespace and splits by any length of whitespace between words.
- reverse(): Flips the order of words in the list.
- join(): Concatenates words with a single space.

s = "  hello world  "
- ls = ["hello", "world"]  # Spaces are gone
- ls = ["world", "hello"]  # Order is reversed
- return "world hello"

Complexity:
- Time: O(n) -> split, reverse, and join all take linear time.
- Space: O(n) -> To store the list of words.
'''
def reverseWords(s: str) -> str:
    ls = s.split()
    ls.reverse()
    return " ".join(ls)