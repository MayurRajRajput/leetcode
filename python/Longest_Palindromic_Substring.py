# Longest Palindromic Substring
""" 
Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ans = max(ans,expand(s,i,i),expand(s,i,i+1),key=len)
        return ans
def expand(s,i,j):
    while i>=0 and j<len(s) and s[i] == s[j]:
        i-=1
        j+=1
    return s[i+1:j]
s = "babad"
sol = Solution()
res = sol.longestPalindrome(s)
print(res)
""" 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""