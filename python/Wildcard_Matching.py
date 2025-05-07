# Wildcard Matching
""" 
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        accept = state
        states = {0}
        for char in s:
            states = {transfer.get((at, token)) for at in states if at is not None for token in (char, '*', '?')}
        return accept in states
s = "aa"
p = "a"
sol = Solution()
res = sol.isMatch(s,p)
print(res)
""" 
Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 
"""