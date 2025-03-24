# Move Zeroes
""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i!=k:
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = temp
                k+=1     
        return nums
nums = [0,1,0,3,12]
sol = Solution()
res = sol.moveZeroes(nums)
print(res)
""" 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""