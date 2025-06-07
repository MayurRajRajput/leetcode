# Unique Binary Search Trees II
""" 
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        memo = {}
        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            trees = []
            if start > end:
                trees.append(None)
                return trees
            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)

# Helper function to serialize the tree (level-order traversal)
def serialize(root: TreeNode) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Usage
n = 3
sol = Solution()
trees = sol.generateTrees(n)
serialized_trees = [serialize(tree) for tree in trees]
for tree in serialized_trees:
    print(tree)
""" 
Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 
"""