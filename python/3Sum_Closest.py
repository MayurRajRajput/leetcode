# 3Sum Closest
""" 
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closed_sum = float('inf')
        for i in range(len(nums)-2):
            left,right = i + 1,len(nums)-1
            while left<right:
                curr = nums[i] +nums[left] +nums[right]
                if abs(curr-target)<abs(closed_sum-target):
                    closed_sum = curr
                if curr <target:
                    left +=1
                    
                elif curr > target:
                    right -=1
                else:
                    return curr
        return closed_sum  
nums = [-1,2,1,-4]
target = 1
sol = Solution()
res = sol.threeSumClosest(nums,target)
print(res)
""" 
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
"""