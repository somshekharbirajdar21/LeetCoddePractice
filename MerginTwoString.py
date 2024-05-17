"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        shortStr = min(len(word1), len(word2))
        finalStr = ""
        for i in range(shortStr):
            finalStr = finalStr+word1[i]+word2[i]
        
        if len(word1) > len(word2):
            finalStr = finalStr+word1[shortStr:]
        else:
            finalStr = finalStr+word2[shortStr:]
        return finalStr

print(Solution().mergeAlternately("abcd","pq"))