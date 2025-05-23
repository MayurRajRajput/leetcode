# Diameter of Binary Tree
""" 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node,res):
            if not node:
                return 0
            left = diameter(node.left,res)
            right = diameter(node.right,res)
            res[0] = max(res[0],left+right)
            return max(left,right)+1
        res=[0]
        diameter(root,res)
        return res[0]
root=TreeNode(1)
root.left=TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()
res=sol.diameterOfBinaryTree(root)
print(res)     
""" 
Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""