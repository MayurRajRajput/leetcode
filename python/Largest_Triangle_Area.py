# Largest Triangle Area
""" 
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
"""
from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                for k in range(j+1,n):
                    x3,y3 = points[k]
                    curr = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    if curr>area:
                        area = curr
        return area
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
sol =Solution()
res = sol.largestTriangleArea(points)
print(res)  
""" 
Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 
"""