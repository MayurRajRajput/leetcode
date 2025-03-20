# Excel Sheet Column Number
""" 
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0 
        for char in columnTitle:
            res = res*26+(ord(char)-ord('A')+1)
        return res
columnTitle = "AB"
sol =Solution()
res = sol.titleToNumber(columnTitle)
print(res)
""" 
Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 
"""