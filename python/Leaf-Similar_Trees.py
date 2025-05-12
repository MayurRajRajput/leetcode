# Leaf-Similar Trees
""" 
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.ans1=[]
        self.ans2=[]
        def traversal1(root):
            if root==None:
                return
            traversal1(root.left)
            traversal1(root.right)
            if root.left==None and root.right==None:
                self.ans1.append(root.val)
        def traversal2(root):
            if root==None:
                return
            traversal2(root.left)
            traversal2(root.right)
            if root.left==None and root.right==None:
                self.ans2.append(root.val)
        traversal1(root1)
        traversal2(root2)
        if len(self.ans1)!=len(self.ans2):
            return False
        for i in range(len(self.ans1)):
            if self.ans1[i]!=self.ans2[i]:
                return False
        return True
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

root1_list = [3,5,1,6,2,9,8,None,None,7,4]
root2_list = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

root1 = build_tree(root1_list)
root2 = build_tree(root2_list)

sol = Solution()
res = sol.leafSimilar(root1, root2)
print(res)
""" 
Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 
"""