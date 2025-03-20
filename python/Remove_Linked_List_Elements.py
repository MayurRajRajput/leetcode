# Remove Linked List Elements
""" 
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def removeNode(head:Optional[ListNode],val:int):
            while head and head.val ==val:
                head  = head.next
            ptr =head
            while ptr and ptr.next:
                if ptr.next.val == val:
                    removeval=ptr.next
                    ptr.next=removeval.next 
                else:
                    ptr=ptr.next
            return head
        return removeNode(head,val)
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
head = ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None)))))))
val= 6
sol = Solution()
result = sol.removeElements(head,val)
printList(result)                

""" 
Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""