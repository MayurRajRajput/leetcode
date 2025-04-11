# Remove Nth Node From End of List
""" 
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0,head)
        dummy = res 
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next =dummy.next.next 
        return res.next
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
n=2
sol = Solution()
result = sol.removeNthFromEnd(head,n)
printList(result) 
""" 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
"""