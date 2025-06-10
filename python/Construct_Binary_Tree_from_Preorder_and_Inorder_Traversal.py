# Construct Binary Tree from Preorder and Inorder Traversal
""" 
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        
        def helper(left, right):
            nonlocal index
            if left > right:
                return None
            
            curr = preorder[index]
            index += 1
            node = TreeNode(curr)
            
            if left == right:
                return node
            
            inorder_index = inorder_map[curr]
            node.left = helper(left, inorder_index - 1)
            node.right = helper(inorder_index + 1, right)
            return node
        
        return helper(0, len(inorder) - 1)

# Helper function to verify the tree via inorder traversal
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

# Test input
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

sol = Solution()
root = sol.buildTree(preorder, inorder)
res = inorderTraversal(root)
print(res)  # Should print the inorder input to confirm correctness

"""
Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
"""