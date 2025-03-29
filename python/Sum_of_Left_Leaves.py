# Sum of Left Leaves
""" 
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        queue = deque([(root,False)])
        total = 0
        while queue:
            node,is_left = queue.popleft()
            if is_left and not node.left and not node.right:
                total +=node.val
            if node.left:
                queue.append((node.left,True))
            if node.right:
                queue.append((node.right,False))
        return total
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
result = sol.sumOfLeftLeaves(root)
print(result) 

""" 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 
"""