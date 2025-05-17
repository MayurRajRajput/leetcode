# Smallest Range I
""" 
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

"""
from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)

        if (max_val - min_val) - (2 * k) <= 0 or max_val - min_val == 0:
            return 0
        else:
            return (max_val - min_val) - (2 * k)
nums = [1]
k = 0
sol = Solution()
res = sol.smallestRangeI(nums,k)
print(res) 
""" 
Example 1:

Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
Example 2:

Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
Example 3:

Input: nums = [1,3,6], k = 3
Output: 0
Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
 
"""