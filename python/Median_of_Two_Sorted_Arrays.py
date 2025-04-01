# Median of Two Sorted Arrays
""" 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged.sort()
        total = len(merged)
        if total%2==1:
            return float(merged[total//2])
        else:
            middle1 = merged[total//2-1]
            middle2 =merged[total//2]
            return (float(middle1)+float(middle2)) /2.0
nums1 = [1,3]
nums2 = [2]
sol = Solution()
res = sol.findMedianSortedArrays(nums1,nums2)
print(res)
""" 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
"""