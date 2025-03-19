# Majority Element
"""  
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 """
from typing import List
 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        uni = 0
        for num in nums :
            if count == 0:
                uni=num
            if num == uni:
                count+=1
            else:
                count-=1
        return uni
nums = [3,2,3]
sol =Solution()
res = sol.majorityElement(nums)
print(res)
            
"""
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""