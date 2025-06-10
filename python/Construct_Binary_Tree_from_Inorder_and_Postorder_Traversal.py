# Construct Binary Tree from Inorder and Postorder Traversal
""" 
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

"""
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = len(postorder) - 1
        mp = {val: i for i, val in enumerate(inorder)}
        
        def build(s, e):
            nonlocal idx
            if s > e:
                return None
            root_val = postorder[idx]
            idx -= 1
            root = TreeNode(root_val)
            id = mp[root_val]
            # Build right before left (reverse of preorder)
            root.right = build(id + 1, e)
            root.left = build(s, id - 1)
            return root 
        
        return build(0, len(inorder) - 1)

# Helper: level-order traversal for output validation
def levelOrderTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Test Example 1
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

sol = Solution()
root = sol.buildTree(inorder, postorder)
print(levelOrderTraversal(root))  # Expected: [[3], [9, 20], [15, 7]]

""" 
Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""