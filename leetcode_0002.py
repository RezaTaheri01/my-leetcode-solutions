from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def navigation(self, l):
        if l == None:
            return ""
        return str(l.val) + self.navigation(l.next)

    # Function to create a linked list from a list of values
    def create_linked_list(self, values):
        if not values:
            return None  # Return None if the list is empty
        head = ListNode(values[0])  # Create the head node
        current = head
        for value in values[1:]:
            current.next = ListNode(value)  # Create and link the next node
            current = current.next
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = self.navigation(l1)
        val2 = self.navigation(l2)

        result = str(int(val1[::-1]) + int(val2[::-1]))
        print(result[::-1])
        return self.create_linked_list(list(result[::-1]))


s = Solution()

# Create the linked list from the list of values
head1 = s.create_linked_list([2, 4, 9])
head2 = s.create_linked_list([5, 6, 4, 9])
s.addTwoNumbers(head1, head2)
