# Binary Tree Level Order Traversal
""" 
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
    
        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_level)
        
        return res

# Helper function to build tree from list
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    q = collections.deque([root])
    i = 1
    while i < len(values):
        node = q.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

# Example usage
tree_vals = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_vals)
sol = Solution()
result = sol.levelOrder(root)
print(result)  # Output: [[3], [9, 20], [15, 7]]

""" 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""