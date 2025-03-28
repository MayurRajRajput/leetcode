# Power of Four
""" 
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>0 and n%4==0:
            n//=4
        return n==1
n=16
sol = Solution()
res = sol.isPowerOfFour(n)
print(res)
"""
Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 
"""