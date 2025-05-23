# Same Tree
""" 
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.left,q.left)
        return False
p = TreeNode(1)              
p.right = TreeNode(2)         
p.right.left = TreeNode(3) 
q = TreeNode(1)              
q.right = TreeNode(2)         
q.right.left = TreeNode(3) 
sol = Solution()
res=sol.isSameTree(p,q)
print(res)      

""" 
Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 
"""