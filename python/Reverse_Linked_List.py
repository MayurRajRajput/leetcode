# Reverse Linked List
""" 
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        ptr = head
        while ptr:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node
        return prev
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
sol = Solution()
result = sol.reverseList(head)
printList(result)   


""" 
Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
"""