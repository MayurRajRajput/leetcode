# Merge Two Sorted Lists
""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        ptr =dummy
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        ptr.next = list1 if list1 else list2
        
        
        return dummy.next
        
    
def printList(head:Optional[ListNode]):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    print("->".join(map(str,values)))
print("before merging")
list1 = ListNode(1,ListNode(2,ListNode(4,None))) 
list2 = ListNode(1,ListNode(3,ListNode(4,None))) 
printList(list1)    
printList(list2)    
sol = Solution()
head = sol.mergeTwoLists(list1,list2)
print("after merging")
printList(head)

""" 
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""