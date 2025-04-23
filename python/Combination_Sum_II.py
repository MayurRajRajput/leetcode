# Combination Sum II
""" 
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
from collections import Counter
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, c = [], Counter(candidates)

        def dfs(s, n, res):
            if s == target: return ans.append(res)
            if s > target or n < 1: return
            for i in range(0, c[n]+1): dfs(s+i*n, n-1, res+[n]*i)

        dfs(0, 50, [])
        return ans
candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
result = sol.combinationSum2(candidates,target)
print(result) 
""" 
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
"""