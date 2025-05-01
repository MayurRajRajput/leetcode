# Permutations II
""" 
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for n in nums:
            new_res = []
            for l in res:
                for i in range(len(l)+1):
                    new_res.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n : break
            res = new_res
        return res

nums = [1,1,2]
sol = Solution()
result = sol.permuteUnique(nums)
print(result)  
""" 
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
"""