from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # Set to store values of nodes that are duplicates
        blacklist = set()
        
        # Dummy node to handle edge cases such as head being a duplicate
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        # First pass: Identify all duplicate values
        while current and current.next:
            if current.val == current.next.val:
                blacklist.add(current.val)
            current = current.next

        # Second pass: Rebuild the list, skipping blacklisted values
        current = head
        prev = dummy
        while current:
            if current.val in blacklist:
                # Skip over nodes with duplicate values
                prev.next = current.next
            else:
                # Link nodes without duplicate values
                prev = current
            current = current.next
        
        return dummy.next



# region linked list
head = ListNode(1)
curr = head
for n in [1,2, 2, 3, 4, 5, 5]:
    curr.next = ListNode(n)
    curr = curr.next
# endregion

s = Solution()
result = s.deleteDuplicates(head)

while result:
    print(result.val, end=", ")
    result = result.next
