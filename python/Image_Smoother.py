# Image Smoother
""" 
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
"""
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        for i in range(rows):
            for j in range(cols):
                total_sum = 0
                count = 0

                for k in range(9):
                    ni, nj = i + dx[k], j + dy[k]

                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_sum += img[ni][nj]
                        count += 1
                result[i][j] = total_sum // count

        return result
img = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
res = sol.imageSmoother(img)
print(res)
           
""" 
Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
"""