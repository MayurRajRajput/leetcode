# Max Consecutive Ones
""" 
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        max_1 = 0
        for i in range(n):
            if nums[i] == 1:
                count+=1
            else:
                max_1 = max(max_1,count)
                count =0
        return max(max_1,count)
nums = [1,1,0,1,1,1]
sol = Solution()
res = sol.findMaxConsecutiveOnes(nums)
print(res)
""" 
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""