# Remove Duplicates from Sorted List II
""" 
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            is_duplicate = False

            while current.next and current.val == current.next.val:
                is_duplicate = True
                current = current.next

            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test
head = [1, 2, 3, 3, 4, 4, 5]
linked_head = list_to_linkedlist(head)

sol = Solution()
result_node = sol.deleteDuplicates(linked_head)
result_list = linkedlist_to_list(result_node)

print(result_list)  # Expected: [1, 2, 5]
""" 
Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 
"""