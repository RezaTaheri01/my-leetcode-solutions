from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getTail(self, node):
        length: int = 1
        while node.next:
            node = node.next
            length += 1

        return node, length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        tail, length = self.getTail(head)

        # Remove full rotates and get remain as rotates
        k %= length
        if k == 0:
            return head  # No rotation needed

        # Make it a circular list
        tail.next = head

        # Find new tail (one step before the new head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # New head is the next of new tail
        new_head = new_tail.next
        new_tail.next = None  # Break the cycle

        return new_head
