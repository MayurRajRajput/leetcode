# Island Perimeter
""" 
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    if (j>0 and grid[i][j-1] ==0) or j==0:
                        cnt+=1
                    if(i>0 and grid[i-1][j]==0) or i == 0:
                        cnt+=1
                    if(j<m-1 and grid[i][j+1]==0) or j==m-1:
                        cnt+=1
                    if(i<n-1 and grid[i+1][j]==0) or i==n-1:
                        cnt+=1
        return cnt  
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sol = Solution()
res = sol.islandPerimeter(grid)
print(res)
""" 
Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""