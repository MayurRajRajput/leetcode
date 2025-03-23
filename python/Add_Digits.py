# Add Digits
""" 
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""
class Solution:
    def addDigits(self, num: int) -> int:
        # with Modulus
        if not num:return 0
        elif num%9==0:
            return 9
        else:
            return num%9
        
        # without Modulus
        # while num >=10:
        #     num = sum(int(digit) for digit in str(num))
        # return num
            
num = 38
sol =Solution()
res = sol.addDigits(num)
print(res)    
""" 
Example 1:

Input: num = 22
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""