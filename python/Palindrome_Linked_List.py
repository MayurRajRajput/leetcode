# Palindrome Linked List
""" 
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:return False
        ptr = head
        res=[]
        while ptr:
            res.append(ptr.val)
            ptr=ptr.next
        if res == res[::-1]:
            return True
        return False 
head = ListNode(1,ListNode(2,ListNode(2,ListNode(1,None))))
sol = Solution()
res = sol.isPalindrome(head)
print(res)
""" 
Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
"""