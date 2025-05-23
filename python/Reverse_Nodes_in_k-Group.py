# Reverse Nodes in k-Group
""" 
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,start,end):
        prev,curr = None,start
        while curr!=end:
            nxt = curr.next
            curr.next = prev 
            prev = curr 
            curr = nxt
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count ,temp = 0,head
        while temp and count < k:
            temp =temp.next
            count+=1
        if count<k:
            return head
        new_head = self.reverse(head,temp)
        head.next = self.reverseKGroup(temp,k)
        return new_head
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
k=2
sol = Solution()
result = sol.reverseKGroup(head,k)
printList(result)  
""" 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""