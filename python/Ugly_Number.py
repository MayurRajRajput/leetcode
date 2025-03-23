# Ugly Number
""" 
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""
class solution:
    def isUgly(self,n:int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n%2==0:
                n//=2
            elif n%3==0:
                n//=3
            elif n%5==0:
                n//=5
            else:
                break
        return n==1    
n=6
sol = solution()
res = sol.isUgly(n)
print(res)
        

""" 
Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
 
"""