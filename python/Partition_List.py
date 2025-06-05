# Partition List
""" 
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist, blist = ListNode(), ListNode()
        small, big = slist, blist
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = blist.next
        big.next = None 
        return slist.next
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = [1, 4, 3, 2, 5, 2]
x = 3
linked_head = list_to_linkedlist(head)

sol = Solution()
result_node = sol.partition(linked_head, x)
result_list = linkedlist_to_list(result_node)

print(result_list)  # Expected: [1, 2, 2, 4, 3, 5]

""" 
Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""