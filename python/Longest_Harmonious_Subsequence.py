# Longest Harmonious Subsequence
""" 
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
"""
from collections import Counter
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_length = 0
        for key in freq:
            if key + 1 in freq:
                max_length = max(max_length, freq[key] + freq[key+1])        
        return max_length
nums = [1,3,2,2,5,2,3,7]
sol = Solution()
res = sol.findLHS(nums)
print(res)
""" 
Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

 
"""