# Minimum Distance Between BST Nodes
""" 
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res,root.val-self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
root=TreeNode(4)
root.left=TreeNode(2)
root.right = TreeNode(6)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)

sol = Solution()
res=sol.minDiffInBST(root)
print(res)
""" 
Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
"""