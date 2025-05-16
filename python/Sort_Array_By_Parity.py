# Sort Array By Parity
""" 
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
 
"""
from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        my_list = []

        for i in nums:
            if i % 2 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)

        my_list.extend(even_nums)
        my_list.extend(odd_nums)

        return my_list
nums = [3,1,2,4]
sol = Solution()
res = sol.sortArrayByParity(nums)
print(res)
""" 
Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 
"""