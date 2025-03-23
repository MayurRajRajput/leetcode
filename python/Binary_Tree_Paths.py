# Binary Tree Paths
""" 
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:return []
        return [str(root.val)+'->'+path 
                for kid in (root.left,root.right)
                for path in self.binaryTreePaths(kid)] or [str(root.val)]
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right = TreeNode(5)

sol = Solution()
res=sol.binaryTreePaths(root)
print(res)

""" 
Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
"""