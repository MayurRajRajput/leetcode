# Rotate List
""" 
Given the head of a linked list, rotate the list to the right by k places.

"""
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Get the length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Make it a circular list
        tail.next = head

        # Find the new tail: (length - k) steps from current tail
        steps_to_new_head = length - k
        new_tail = tail
        while steps_to_new_head:
            new_tail = new_tail.next
            steps_to_new_head -= 1

        # Break the circle and return new head
        new_head = new_tail.next
        new_tail.next = None
        return new_head

# Helper function to print the list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test case
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
result = sol.rotateRight(head, 2)  # Use rotateRight instead of reverseList
printList(result)

 
""" 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
"""