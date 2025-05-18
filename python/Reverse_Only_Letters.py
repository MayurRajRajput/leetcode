# Reverse Only Letters
""" 
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s, i, j = list(s), 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        return "".join(s)
s = "ab-cd"
sol = Solution()
result = sol.reverseOnlyLetters(s)
print(result) 
""" 
Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
"""