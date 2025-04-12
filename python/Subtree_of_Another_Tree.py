# Subtree of Another Tree
""" 
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None :
            return True
        if root == None :
            return False
        if self.same(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            
    def same(self , r , s):
        if r == None and s == None :
            return True
        if r and s and r.val == s.val:
            return self.same(r.right , s.right) and self.same(r.left , s.left)  
        return False
root = TreeNode(3)              
root.left = TreeNode(4)         
root.right = TreeNode(5)         
root.left.left = TreeNode(1) 
root.left.right = TreeNode(2) 
subRoot = TreeNode(4)              
subRoot.left = TreeNode(1)         
subRoot.right = TreeNode(2) 
sol = Solution()
res=sol.isSubtree(root,subRoot)
print(res)
""" 
Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""