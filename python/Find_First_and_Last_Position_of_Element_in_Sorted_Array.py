# Find First and Last Position of Element in Sorted Array
""" 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,is_searching_left):
            l,r = 0,len(nums)-1
            idx=-1
            while l<=r:
                m = (l+r)//2
                if nums[m]>target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    idx = m
                    if is_searching_left:
                        r=m-1
                    else:
                        l=m+1
            return idx
        l = binary_search(nums,target,True)
        r = binary_search(nums,target,False)
        return [l,r]
nums = [5,7,7,8,8,10]
target = 8
sol = Solution()
res=sol.searchRange(nums,target)
print(res)
""" 
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""