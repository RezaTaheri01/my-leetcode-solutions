# Todo: cleaner solution
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        # add all nodes to stack list
        current = head
        stack: list[ListNode] = []
        while current:
            stack.append(current)
            current = current.next
         
        # remove (length % k) from tail   
        cut_index = len(stack) % k
        if cut_index != 0:
            next_group = stack[-cut_index] # None or length % k items from right side
            stack = stack[:-cut_index]
        else:
            next_group = None
        
        # now reverse each section
        while stack:
            group_head = stack[-1]
            for _ in range(k - 1):
                node = stack.pop()
                node.next = stack[-1]
            node = stack.pop()
            node.next = next_group

            if stack:
                next_group = group_head
            else:
                head = group_head

        return head


s = Solution()


head = ListNode(1)
current = head
for num in [2,3,4,5]:
    current.next = ListNode(num)
    current = current.next

reverse_head = s.reverseKGroup(head, 5)
