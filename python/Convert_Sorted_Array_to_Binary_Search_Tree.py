# Convert Sorted Array to Binary Search Tree
""" 
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""
from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
       if not nums:
           return None
       mid = len(nums)//2
       root =TreeNode(nums[mid])
       root.left = self.sortedArrayToBST(nums[:mid])
       root.right=self.sortedArrayToBST(nums[mid+1:]) 
       return root
#bst to list using level-order-traversal(bfs) to print
def bst_to_list(root:Optional[TreeNode])->List[Optional[int]]:
    if not root: return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

nums = [-10,-3,0,5,9]
sol =Solution()
root = sol.sortedArrayToBST(nums)
print(bst_to_list(root))
  
""" 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""