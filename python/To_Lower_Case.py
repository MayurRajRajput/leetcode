# To Lower Case
""" 
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for i in s:
            temp = ord(i)
            if 65<=temp<=90:
                a = temp-65
                res+=chr(a+97)
            else:
                res+=i
        return res
s = "Hello"
sol =Solution()
res = sol.toLowerCase(s)
print(res) 
""" 
Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
"""