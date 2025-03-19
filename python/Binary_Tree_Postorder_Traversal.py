# Binary Tree Postorder Traversal
""" 
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res = []
      def dfs(node):
          if not node:return 
          dfs(node.left)
          dfs(node.right)
          res.append(node.val)
      dfs(root)
      return res
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol =Solution()
res = sol.preorderTraversal(root)
print(res)
"""  
Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]
"""