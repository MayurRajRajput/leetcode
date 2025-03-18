# Linked List Cycle
""" 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        onestep =head
        twostep = head
        while twostep is not None and twostep.next is not None:
            onestep = onestep.next
            twostep = twostep.next.next
            if onestep == twostep:
                return True
        return False
def createLinkedListWithCycle(values,pos):
    if not values:return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos !=-1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


head = createLinkedListWithCycle([3,2,0,-3],1)
sol = Solution()
result = sol.hasCycle(head)
print(result) 
""" 
Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""