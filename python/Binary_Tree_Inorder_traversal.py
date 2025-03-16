# Binary Tree Inorder Traversal
""" 
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root: return []
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)
        return res
root = TreeNode(1)              
root.right = TreeNode(2)         
root.right.left = TreeNode(3) 
sol = Solution()
res=sol.inorderTraversal(root)
print(res)
""" 
Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]
"""