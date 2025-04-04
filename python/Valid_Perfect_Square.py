# Valid Perfect Square
""" 
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x *x >num:
            x = (x+num//x)//2
        return x*x == num
num = 16
sol = Solution()
res = sol.isPerfectSquare(num)
print(res)

""" 
Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""