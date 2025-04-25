# Binary Number with Alternating Bits
""" 
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)
        num = num[2:]
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                return False
        return True
n = 5
sol = Solution()
result = sol.hasAlternatingBits(n)
print(result)
""" 
Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 
"""