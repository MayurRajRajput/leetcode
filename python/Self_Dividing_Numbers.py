# Self Dividing Numbers
""" 
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

"""
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def divisible(n):
            for d in str(n):
                if d == '0' or n%int(d)>0:
                    return False
            return True
        res = []
        for n in range(left,right+1):
            if divisible(n):
                res.append(n)
        return res
left = 1 
right = 22
sol = Solution()
res = sol.selfDividingNumbers(left,right)
print(res) 
""" 
Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]
"""