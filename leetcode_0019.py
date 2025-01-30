from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(2n) => O(n)
class Solution:
    def getTail(self, node): 
        length: int = 1
        while node.next:
            node = node.next
            length += 1

        return node, length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        tail, length = self.getTail(head)

        if n == length:
            head = head.next
            return head

        # find n + 1 node from the end
        nth_node = head
        for _ in range(length - n - 1):
            nth_node = nth_node.next


        nth_node.next = nth_node.next.next

        return head
