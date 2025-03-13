# Remove Duplicates from Sorted List
""" 
Easy
Topics
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next 
        return head
    
def print_list(head:Optional[ListNode]):
    values = []
    while head:
        values.append(head.val)
        head =head.next 
    print("->".join(map(str,values)))
head = ListNode(1,(ListNode(1,ListNode(2,None))))
print("before removing duplicates: ")
print_list(head)
sol = Solution()
new_head = sol.deleteDuplicates(head)
print("after removing duplicates: ")
print_list(new_head)
""" 
 Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""