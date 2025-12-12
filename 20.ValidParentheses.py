'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false
'''
def isValid(self, s: str) -> bool:
    balanced = []
    def isProperlyClosed(opening: str, closing: str) -> bool:
        if opening == '(' and closing == ')': return True
        elif opening == '[' and closing == ']': return True
        elif opening == '{' and closing == '}': return True
        return False

    for parentheses in s:
        if parentheses == '(' or parentheses == '{' or parentheses == '[':
            balanced.append(parentheses)
        else:
            if not balanced or not isProperlyClosed(balanced.pop(), parentheses): return False

    return not balanced