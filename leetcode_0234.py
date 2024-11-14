from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li: list = []

        # navigate on linked list
        while head:
            li.append(head.val)
            head = head.next

        return li == li[::-1]
