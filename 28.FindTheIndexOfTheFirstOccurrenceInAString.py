'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
def strStr(haystack: str, needle: str) -> int: #T: O(n + m), S: O(m)
    def buildLPS(s):
        n=len(s)
        lps = [0]*n
        prevlps, i = 0, 1
        while i<n:
            if s[i] == s[prevlps]:
                prevlps+=1
                lps[i] = prevlps
                i+=1
            else:
                if prevlps != 0:
                    prevlps = lps[prevlps-1]
                else:
                    lps[i] = 0
                    i+=1     
        return lps
    lps = buildLPS(needle)
    i, j = 0, 0
    while i<len(haystack):
        if haystack[i] == needle[j]:
            i,j = i+1, j+1
        else:
            if j == 0:
                i+=1
            else:
                j = lps[j-1]
        if j == len(needle):
            return i-len(needle)
    return -1