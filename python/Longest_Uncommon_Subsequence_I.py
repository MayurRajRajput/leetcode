# Longest Uncommon Subsequence I
""" 
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.
"""
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if  a==b:return -1
        else:
            return max(len(a),len(b))
a = "aba"
b = "cdc"
sol =Solution()
res = sol.findLUSlength(a,b)
print(res)
""" 
Example 1:

Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
"""