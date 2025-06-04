# Subsets
""" 
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer = [[]]
        for num in nums:
            n = len(outer)
            for i in range(n):
                internal = outer[i] + [num]
                outer.append(internal)
        return outer
nums = [1,2,3]
sol = Solution()
length = sol.subsets(nums)
print(length)
""" 
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""