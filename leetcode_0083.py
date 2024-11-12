# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen: dict = {}
        current_node = head
        while current_node:
            if current_node.val not in seen:
                seen[current_node.val] = True
            current_node = current_node.next

        first = True
        current_node = None
        for num in seen.keys():
            if not first:
                current_node.next = ListNode(num)
                current_node = current_node.next
            else:
                first = not first
                head = ListNode(num)
                current_node = head

        return head
