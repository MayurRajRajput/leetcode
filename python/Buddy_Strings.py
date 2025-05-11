# Buddy Strings
""" 
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(goal) != n:
            return False
        if s==goal:
            temp = set(s)
            return len(temp) < len(goal)
        i = 0
        j = n-1
        while i<j and s[i] == goal[i]:
            i+=1
        while j>=0 and s[j] == goal[j]:
            j-=1
        if i<j:
            s_list = list(s)
            s_list[i],s_list[j] = s_list[j],s_list[i]
            s = ''.join(s_list)
        return s == goal
s = "ab"
goal = "ba"
sol = Solution()
result = sol.buddyStrings(s,goal)
print(result) 
""" 
Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 
"""