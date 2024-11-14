from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        middle = head

        while head:
            if counter != 0 and counter % 2 == 0:
                middle = middle.next

            head = head.next
            counter += 1

        if counter % 2 == 0:  # means that the len of linked list is even
            middle = middle.next
        return middle
