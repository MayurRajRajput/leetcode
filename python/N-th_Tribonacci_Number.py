# N-th Tribonacci Number
""" 
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        Tribonacci = [0] * (n + 1)
        Tribonacci[0] = 0
        Tribonacci[1] = 1
        Tribonacci[2] = 1
        for i in range(3, n + 1):
            Tribonacci[i] = Tribonacci[i-1] + Tribonacci[i-2] + Tribonacci[i-3]
        return Tribonacci[n]
n = 4
sol = Solution()
res = sol.tribonacci(n)
print(res)
""" 
Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 
"""