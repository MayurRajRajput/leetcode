# Summary Ranges
""" 
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums:return res
        start = nums[0]
        for i in range(1,len(nums)+1):
            if i==len(nums) or nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i-1]}")
                if i <len(nums):
                    start = nums[i]
        return res      
nums = [0,1,2,4,5,7]
sol =Solution()
res = sol.summaryRanges(nums)
print(res)
""" 
Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 
"""