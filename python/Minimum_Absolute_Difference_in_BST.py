# Minimum Absolute Difference in BST
""" 
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = -float('inf')
        def in_order_traverse(node):
            if not node:
                return
            in_order_traverse(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            in_order_traverse(node.right)
        in_order_traverse(root)
        return self.min_diff
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
sol =Solution()
res = sol.getMinimumDifference(root)
print(res)
""" 
Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
"""