# Rotate Image
""" 
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        swapped = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                v1 = f"{i}-{j}"
                v2 = f"{j}-{i}"
                if i != j and v1 not in swapped and v2 not in swapped:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    swapped.add(v1)
                    swapped.add(v2)
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j],matrix[i][j]
        return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
res = sol.rotate(matrix)
print(res)
""" 
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""