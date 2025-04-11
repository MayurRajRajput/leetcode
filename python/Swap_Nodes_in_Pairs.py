# Swap Nodes in Pairs
""" 
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        temp = head
        while temp and temp.next:
            data = temp.val
            temp.val = temp.next.val
            temp.next.val = data
            temp= temp.next.next
        return head
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
sol = Solution()
result = sol.swapPairs(head)
printList(result)
""" 
Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 
"""