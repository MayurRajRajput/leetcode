# Convert a Number to Hexadecimal
""" 
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
"""
class Solution:
    def toHex(self, num: int) -> str:
        return hex(num & 0xFFFFFFFF)[2:]
num = -1
sol = Solution()
res = sol.toHex(num)
print(num)
""" 
Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
 
"""