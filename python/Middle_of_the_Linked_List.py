# Middle of the Linked List
""" 
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Helper function to create linked list from Python list
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list from given node
def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# Test Example 1
head = create_linked_list([1,2,3,4,5])
sol = Solution()
res = sol.middleNode(head)
print_linked_list(res)
""" 
Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
"""