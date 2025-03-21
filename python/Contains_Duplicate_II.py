# Contains Duplicate II
""" 
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        for idx in range(len(nums)):
            if nums[idx] in hset and abs(idx-hset[nums[idx]])<=k:
                return True
            hset[nums[idx]]=idx
        return False

nums = [1,2,3,1]
k = 3     
sol =Solution()
res = sol.containsNearbyDuplicate(nums,k)
print(res)  
""" 
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 
"""