# Number of Segments in a String
""" 
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
"""
class Solution:
    def countSegments(self,s:str)->int:
        if not s :
            return 0
        words = s.split()
        return len(words)
s = "Hello, my name is John"
sol =Solution()
res = sol.countSegments(s)
print(res)

""" 
Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
 
"""