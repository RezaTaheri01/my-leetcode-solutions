from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # Early Stop
            return head

        node = head
        head_new = node.next
        node_prev = None

        while node and node.next:
            node_next = node.next
            node.next = node_next.next
            node_next.next = node

            if node_prev:
                node_prev.next = node_next
            node_prev = node
            
            node = node.next

        return head_new
