# Permutations
""" 
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        res = []
        for _ in range(len(nums)):
            n=nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            res.extend(perms)
            nums.append(n)
        return res
nums = [1,2,3]
sol = Solution()
result = sol.permute(nums)
print(result)    
""" 
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""