'''
Approach: Since the string can have spaces at the end, we will use a variable to point at the last valid index of the string. Then, we will traverse all the string, everytime
the char in s is different than a space, we add 1 to a counter. Otherwise, we reset the counter to zero. At end return the counter
'''
def lengthOfLastWord(s: str) -> int: #T: O(n), S: O(1)
    n = len(s)
    leng = n-1
    while s[leng] == ' ': leng -= 1
    letter_count = 0
    for i in range(leng+1):
        if s[i] != ' ':
            letter_count+=1
        else:
            letter_count=0
    return letter_count 