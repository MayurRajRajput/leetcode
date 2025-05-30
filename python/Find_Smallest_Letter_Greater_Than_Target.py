# Find Smallest Letter Greater Than Target
""" 
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
 
"""
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1] or target <letters[0]:
            return letters[0]
        l,h=0,len(letters)-1
        while (l<=h):
            m=l+(h-l)//2
            if letters[m]<=target:
                l=m+1
            if target < letters[m]:
                h = m-1
        return letters[l] 
letters = ["c","f","j"]
target = "a"
sol = Solution()
res = sol.nextGreatestLetter(letters,target)
print(res) 
""" 
Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 
"""