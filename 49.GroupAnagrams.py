'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
Approach: We can say that 2 or more words are anagrams to each other if they share the same letter frequency. A dictionary can be used to store the frequency counter as key
and a list with all the words sharing the same frequency counter as values. Since a dictionary only allows to use unmutable objects as keys, instead of building dictionaries per word
we will build tuples. 
Each word consists of lowercase English letters, so the array will have a fixed size of 26 elements. The number at 0th index will represent the frequency of the letter a, number at 1th index corresponds to
letter b, and so on. Everytime we compute the frequency of a word, we convert that list into a tuple, this will be the key in the dictionary and the word one of its possible values. 
At the end we will return the list of the values 
''' 
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_dic = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        key = tuple(count)
        anagram_dic[key].append(s)
    return list(anagram_dic.values())  