# Increasing Order Search Tree
""" 
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build a binary tree from level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Print the transformed tree in list form
def print_right_skewed_tree(node: Optional[TreeNode]):
    result = []
    while node:
        result.append(node.val)
        node = node.right
    print(result)

# The increasingBST logic
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            nonlocal current
            if not node:
                return
            inorder(node.left)
            node.left = None
            current.right = node
            current = node
            inorder(node.right)

        dummy = TreeNode(-1)
        current = dummy
        inorder(root)
        return dummy.right

# Example usage
root_list = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = build_tree(root_list)
sol = Solution()
res = sol.increasingBST(root)
print_right_skewed_tree(res)
""" 
Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""