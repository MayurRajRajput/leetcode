# Add Two Numbers
""" 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res =dummy
        total = carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total +=l1.val
                l1 = l1.next
            if l2:
                total +=l2.val
                l2 = l2.next
            num = total%10
            carry = total//10
            dummy.next = ListNode(num)
            dummy = dummy.next
        return res.next
def printList(l):
    res = []
    while l:
        res.append(l.val)
        l = l.next
        
    return "->".join(map(str,res))
l1 = ListNode(2,ListNode(4,ListNode(3,None)))
l2 = ListNode(5,ListNode(6,ListNode(4,None)))
sol =Solution()
res = sol.addTwoNumbers(l1,l2)
print(printList(res)) 
""" 
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
"""