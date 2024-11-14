from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # navigate on linked list
        # 1 => 2 => 3 => None  to  None <= 1 <= 2 <= 3
        rev_head = None
        while head:
            new_node = ListNode(head.val, rev_head)
            rev_head = new_node
            head = head.next

        return rev_head
