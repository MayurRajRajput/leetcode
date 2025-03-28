# First Unique Character in a String
""" 
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
import collections 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hset= collections.Counter(s)
        for idx in range(len(s)):
            if hset[s[idx]==1]:
                return idx
        return -1
s = "leetcode"
sol =Solution()
res = sol.firstUniqChar(s)
print(res) 

""" 
Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 
"""