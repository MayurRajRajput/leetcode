# Ransom Note
""" 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpha = [0]*26
        for c in ransomNote:
            idx = ord(c)-ord('a')
            i =  magazine.find(c,alpha[idx])
            if i ==-1:
                return False
            alpha[idx] = i+1
        return True
ransomNote = "a"
magazine = "b"
sol = Solution()
res = sol.canConstruct(ransomNote,magazine)
print(res)
""" 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""