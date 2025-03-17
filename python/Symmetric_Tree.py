# Symmetric Tree

""" 
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if not p and  not q:
                return True
            if not p or not q :
                return False
            return p.val == q.val and isSame(p.left,q.right) and isSame(p.right,q.left)
        
        return isSame(root.left,root.right)
                
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
 
sol = Solution()
res=sol.isSymmetric(root)
print(res)
""" 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""