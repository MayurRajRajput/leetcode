# Reverse Vowels of a String
""" 
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        st = list(s)
       
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l,r = 0 , len(st)-1
        while l<r:
            while l<r and st[l] not in vowels:
                l+=1
            while l<r and st[r] not in vowels:
                r-=1
            if l<r:
                st[l],st[r] = st[r],st[l]
                l+=1
                r-=1            
            
                
        return "".join(st)


s = "IceCreAm"
sol = Solution()
res = sol.reverseVowels(s)
print(res) 
""" 
Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""