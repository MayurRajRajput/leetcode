# Spiral Matrix II
""" 
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

"""
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x, y, dx, dy = 0, 0, 1, 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n * n):
            res[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or res[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res
n = 3
sol = Solution()
res = sol.generateMatrix(n)
print(res)
""" 
Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 
"""