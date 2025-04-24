# Valid Palindrome II
""" 
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(sub):
            if sub==sub[::-1]:
                return True
            return False
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return palindrome(s[l:r]) or palindrome(s[l+1:r+1])
            l+=1
            r-=1
        return True
s = "aba"
sol = Solution()
res = sol.validPalindrome(s)
print(res)
""" 
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 
"""