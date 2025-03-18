# Pascal's Triangle II
""" 
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(rowIndex):
            dummy_row =[0]+res[-1]+[0]
            row=[]
            for i in range(len(res[-1])+1):
                row.append(dummy_row[i]+dummy_row[i+1])
            res.append(row)                    
        return res[rowIndex]   
    
rowIndex = 3
sol = Solution()
result = sol.getRow(rowIndex)
print(result)             
""" 
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 
"""