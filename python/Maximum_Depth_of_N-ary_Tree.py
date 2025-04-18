# Maximum Depth of N-ary Tree
""" 
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
from typing import Optional,List
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children or []
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)

node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
root = Node(1, [node3, node2, node4])

sol =Solution()
res = sol.maxDepth(root)
print(res)
""" 
Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
 
"""