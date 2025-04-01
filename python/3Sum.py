# 3Sum

""" 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from collections import defaultdict
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num<0:
                negative[num]+=1
            elif num > 0 :
                positive[num]+=1
            else:
                zeros+=1
        res = []
        if zeros:
            for n in negative:
                if -n in positive:
                    res.append((0,n,-n))
                if zeros > 2:
                    res.append((0,0,0))
        for set1,set2 in ((negative,positive),(positive,negative)):
            set1Items = list(set1.items())
            for i,(j,k) in enumerate(set1Items):
                for j2,k2 in set1Items[i:]:
                    if j!=j2 or (j==j2 and k>1):
                        if -j-j2 in set2:
                            res.append((j,j2,-j-j2))
        return res             
    
nums = [-1,0,1,2,-1,-4]
sol = Solution()
res = sol.threeSum(nums)
print(res)
""" 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
"""