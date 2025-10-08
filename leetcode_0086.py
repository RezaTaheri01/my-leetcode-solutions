from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Add a temporary head
        new_head = ListNode(-101)  # -100 <= Node.val <= 100
        new_head.next = head

        read_node = new_head
        read_node_prev = None
        write_node = None

        while read_node:
            if read_node.val < x:
                if write_node is not None:
                    # Add prev.next to read.next
                    read_node_prev.next = read_node.next

                    write_node_next = write_node.next
                    write_node.next = read_node

                    read_node.next = write_node_next

                write_node = read_node

            read_node_prev = read_node
            read_node = read_node.next

        return new_head.next

    def walkthrough(self, node: Optional[ListNode]):
        if not node:
            return
        print(node.val, end=", ")
        self.walkthrough(node.next)


numbers, x = [1, 4, 3, 2, 5, 2], 3
# numbers, x = [2, 1], 2
# numbers, x = [5, 7, 2, 2, 1, 1], 4

# Create a Link List
head = ListNode(numbers[0])
temp = head
for num in numbers[1:]:
    temp.next = ListNode(num)
    temp = temp.next

s = Solution()
head = s.partition(head, x)
s.walkthrough(head)
