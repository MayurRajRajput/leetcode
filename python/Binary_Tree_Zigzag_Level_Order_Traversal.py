# Binary Tree Zigzag Level Order Traversal
""" 
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        is_left_to_right = True
        while queue:
            level_size = len(queue)
            current_level = [0] * level_size
            for i in range(level_size):
                node = queue.popleft()
                index = i if is_left_to_right else level_size - 1 - i
                current_level[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
            is_left_to_right = not is_left_to_right
        return result

# Helper to build a binary tree from list input
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test input
tree_vals = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_vals)
sol = Solution()
result = sol.zigzagLevelOrder(root)
print(result)  # Output: [[3], [20, 9], [15, 7]]

""" 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
"""