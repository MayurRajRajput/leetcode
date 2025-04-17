# Maximum Product of Three Numbers
""" 
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        smallestTwo = [float('inf')]*2
        largestThree = [float('-inf')]*3
        for num in nums:
            if num <= smallestTwo[0]:
                smallestTwo[0] = num
                smallestTwo.sort(reverse=True)
            if num >= largestThree[0]:
                largestThree[0] = num
                largestThree.sort()
        return max(smallestTwo[0]*smallestTwo[1]*largestThree[2], 
                   largestThree[0]*largestThree[1]*largestThree[2])
nums = [1,2,3]
sol = Solution()
result = sol.maximumProduct(nums)
print(result) 
"""  
Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""