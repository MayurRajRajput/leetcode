# Valid Anagram
""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) !=len(t) : return False
        # map1 = {}
        # for idx in s:
        #     map1[idx] = map1.get(idx,0)+1
        # for idx in t:
        #     if idx in map1:
        #         map1[idx]-=1
        #         if map1[idx]==0:
        #             del map1[idx]
        #     else:
        #         return False
        # return len(map1)==0
            
            
            # optimized
        if len(s) !=len(t) : return False
        map = {}
        for i in range(len(s)):
            map[s[i]]= map.get(s[i],0)+1
            map[t[i]] = map.get(t[i],0)-1
        return all(count == 0  for count in map.values())
      
s = "anagram" 
t = "nagaram"
sol = Solution()
result = sol.isAnagram(s,t)
print(result)
""" 
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
"""