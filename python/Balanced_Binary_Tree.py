# Balanced Binary Tree
""" 
Given a binary tree, determine if it is height-balanced.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
    def height(self,node:TreeNode) ->int:
        if not node:
            return 0
        leftheight = self.height(node.left)
        if leftheight==-1:
            return -1
        rightheight = self.height(node.right)
        if rightheight==-1:
            return -1
        if abs(leftheight-rightheight) >1:
            return -1
        return max(leftheight,rightheight)+1
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
 
sol = Solution()
res=sol.isBalanced(root)
print(res)
""" 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

"""