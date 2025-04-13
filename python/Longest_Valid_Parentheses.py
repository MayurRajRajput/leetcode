# Longest Valid Parentheses
""" 
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        l=['0']*len(s)
        for ind,i in enumerate(s):
            if i=='(':
                stack.append(ind)
            else:
                if stack:
                    l[stack.pop()]='1'
                    l[ind]='1'
        return max(len(i) for i in ''.join(l).split('0'))
s = "(()"
sol = Solution()
res = sol.longestValidParentheses(s)
print(res) 
""" 
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""