'''
Simulates the process of adding two numbers from right to left (least significant bit to most significant bit), handling the carry at each step.

Since binary numbers are added starting from the end, we use two pointers (i and j) initialized at the last indices of strings a and b.
In binary addition:
0 + 0 = 0
0 + 1 = 1
1 + 1 = 0 (carry 1)
1 + 1 + 1 (with carry) = 1 (carry 1)
The loop ensures that we continue as long as:
-There are digits left in string a or b
-There is a leftover carry from the previous sum (e.g., 1+1 at the very first position).
Total: bitA + bitB + carry
Current Bit: total % 2 (This gives the remainder: 0 or 1)
Next Carry: total // 2 (This gives 1 if the total was 2 or 3, otherwise 0).
'''
def addBinary(a: str, b: str) -> str:
        i,j = len(a)-1, len(b)-1
        res = []
        carry = 0
        while i>=0 or j>=0 or carry:
            bitA = int(a[i]) if i>=0 else 0
            bitB = int(b[j]) if j>=0 else 0
            total = bitA+bitB+carry
            res.append(str(total%2))
            carry = total//2
            i,j = i-1, j-1
        return "".join(reversed(res))