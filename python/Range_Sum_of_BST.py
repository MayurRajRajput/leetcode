# Range Sum of BST
""" 
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.total_sum += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
        self.total_sum = 0
        dfs(root)
        return self.total_sum
# Helper function to build the example tree:
def build_tree():
    return TreeNode(10,
                    TreeNode(5,
                             TreeNode(3),
                             TreeNode(7)),
                    TreeNode(15,
                             None,
                             TreeNode(18)))

root = build_tree()
sol = Solution()
print(sol.rangeSumBST(root, 7, 15))  

""" 
Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""