# Find Mode in Binary Search Tree
""" 
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:return []
        self.mode = []
        self.max_count = 0
        self.prev = None
        self.count = 0
        self.inorder(root)
        return self.mode
    def inorder(self,root):
        if root is None:return
        self.inorder(root.left)
        if self.prev is None:
            self.prev = root.val
            self.count =1
        elif self.prev == root.val:
            self.count+=1
        else:
            self.prev =root.val
            self.count =1
        if self.count > self.max_count:
            self.max_count = self.count
            self.mode = [root.val]
        elif self.count == self.max_count:
            self.mode.append(root.val)
        self.inorder(root.right)
root=TreeNode(1)
root.right=TreeNode(2)
root.right.left = TreeNode(2)

sol = Solution()
res=sol.findMode(root)
print(res)
"""
Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 
"""