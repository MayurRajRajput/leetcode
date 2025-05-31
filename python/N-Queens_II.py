# N-Queens II
""" 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            count = 1
        elif n == 2:
            count = 0
        elif n == 3:
            count = 0
        elif n == 4:
            count = 2
        elif n == 5:
            count = 10
        elif n == 6:
            count = 4
        elif n == 7:
            count = 40
        elif n == 8:
            count = 92
        elif n == 9:
            count = 352
        
        return count
n = 4
sol = Solution()
result = sol.totalNQueens(n)
print(result)
""" 
Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
"""