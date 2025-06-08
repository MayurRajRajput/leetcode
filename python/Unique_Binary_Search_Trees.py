# Unique Binary Search Trees
""" 
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

"""
class Solution:
    def numTrees(self, n: int) -> int:
        uniq_tree = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_tree[root - 1] * uniq_tree[nodes - root]
            uniq_tree[nodes] = total
        return uniq_tree[n]
n = 3
sol = Solution()
result = sol.numTrees(n)
print(result)
""" 
Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

"""