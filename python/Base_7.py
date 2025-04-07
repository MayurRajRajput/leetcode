# Base 7
""" 
Given an integer num, return a string of its base 7 representation.
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        base7 = []
        while num > 0:
            base7.append(str(num%7))
            num //= 7
        if negative:
            base7.append('-')
        return ''.join(base7[::-1])
num = 100
sol = Solution()
result = sol.convertToBase7(num)
print(result)   
"""
Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
"""