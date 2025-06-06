# Subsets II
""" 
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            result.append(subset[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        nums.sort()
        result = []
        backtrack(0, [])
        return result
nums = [1,2,2]
sol =Solution()
res = sol.subsetsWithDup(nums)
print(res)
""" 
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
"""