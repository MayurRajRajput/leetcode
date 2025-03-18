# Path Sum
"""  
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -=root.val
        if root.left==None and root.right == None and targetSum ==0:
            return True
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
root = TreeNode(5)              
root.left = TreeNode(4) 
root.right = TreeNode(8)  
       
root.left.left = TreeNode(11)              
root.right.left = TreeNode(13)         
root.right.right = TreeNode(4)
 
root.left.left.left = TreeNode(7) 
root.left.left.right = TreeNode(2) 
root.right.right.right = TreeNode(1)
targetSum = 22
sol = Solution()
res=sol.hasPathSum(root,targetSum)
print(res)      


"""  
Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 
"""