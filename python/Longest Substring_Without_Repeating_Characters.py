# Longest Substring Without Repeating Characters
""" 
Given a string s, find the length of the longest substring without duplicate characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       n = len(s)
       maxlen= 0
       char = set()
       left= 0
       for right in range(n):
            if s[right] not in char:
                char.add(s[right])
                maxlen = max(maxlen,right-left+1)
            else:
                while s[right] in char:
                   char.remove(s[left])
                   left+=1
                char.add(s[right])
       return maxlen 
s = "abcabcbb"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)
""" 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

"""