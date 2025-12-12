'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
'''
def generateParenthesis(n: int) -> list[str]: #T: O(2ⁿ) S: O(n)
    res, sol = [],[]
    def backtrack(o:int,c:int)->None:
        if len(sol) == 2*n:
            res.append("".join(sol))
            return
        if o < n:
            sol.append("(")
            backtrack(o+1,c)
            sol.pop()
        if o > c:
            sol.append(")")
            backtrack(o,c+1)
            sol.pop()
    backtrack(0,0)
    return res
            