# Sort Array By Parity II
""" 
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
"""
from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, n = 0, 1, len(nums)
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
nums = [4,2,5,7]
sol = Solution()
res = sol.sortArrayByParityII(nums)
print(res) 
""" 
Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 
"""