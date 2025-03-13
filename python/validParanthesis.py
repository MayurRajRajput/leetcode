# Valid Parentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
# -------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        map_dic = {')':'(','}':'{',']':'['}
        for char in s:
            if char in map_dic:
                top_element = stack.pop() if stack else '#'
                if map_dic[char] != top_element :
                    return False
            else:
                stack.append(char)
        return not stack
# ----------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dic = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in par_dic.values():
                stack.append(char)
            elif char in par_dic.keys():
                if not stack or par_dic[char] != stack.pop():
                    return False
        
        return not stack
s = "([])"
sol = Solution()
result = sol.isValid(s)
print(result)

""" 
example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true
"""