'''
Approach: 
To evaluate RPN the most standard solution uses an stack. For RPN an operation like ( 2 + 1) * 3 is written like 2 1 + 3 *
The solution pushes numbers onto the stack. When an operator is hit, the last two numbers are popped and applied the operation, and the result is pushed back.

tokens = ["2", "1", "+", "3", "*"]

- "2" is operand -> [2]
- "1" is operand -> [2, 1]
- "+" is operator -> Pop(1), Pop(2) -> Push(2 + 1) -> [3]
- "3" is operand -> [3, 3]
- "*" is operator -> Pop(3), Pop(3) -> Push(3 * 3) -> [9]

Complexity:
- Time: O(n) -> We process each token exactly once.
- Space: O(n) -> In the worst case (all numbers then one operator), the stack stores most of the tokens.
'''
def evalRPN(tokens: list[str]) -> int:
    stk = []
    ops = { "+": lambda a,b: a + b, #instead of using a chain of if elif else
            "-": lambda a,b: a - b, 
            "*": lambda a,b: a * b, 
            "/": lambda a,b: int(a/b)}
    for token in tokens:
        if token in ops:
            b,a = stk.pop(), stk.pop() # first pop takes out the second operand, second pop takes out first operand
            stk.append(ops[token](a,b))
        else:
            stk.append(int(token))
    return stk.pop()