# Combination Sum
""" 
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def cal(i,s,curr):
            if i > len(candidates)-1:
                return
            elif s>candidates[i]:
                curr.append(candidates[i])
                cal(i,s-candidates[i],curr)
                curr.pop()
                cal(i+1,s,curr)
            elif s==candidates[i]:
                curr.append(candidates[i])
                out.append(curr[::])
                curr.pop()
                cal(i+1,s,curr)
            else:
                cal(i+1,s,curr)
        curr = []
        cal(0,target,curr)
        return out
candidates = [2,3,6,7]
target = 7
sol = Solution()
result = sol.combinationSum(candidates,target)
print(result)  
""" 
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 
"""