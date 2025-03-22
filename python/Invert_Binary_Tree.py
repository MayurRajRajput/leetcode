# Invert Binary Tree
""" 
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional,List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            ptr = root.left
            root.left = root.right
            root.right = ptr
            self.invertTree(root.left)    
            self.invertTree(root.right)
            
        return root    
       
def bst_to_list(root:Optional[TreeNode])->List[Optional[int]]:
    if not root: return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right= TreeNode(9)

sol =Solution()
res = sol.invertTree(root)
print(bst_to_list(root))
""" 
Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""