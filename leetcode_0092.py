from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right <= left:  # no need to change anything
            return head

        tail = None  # after right
        rev_mid = None  # between left and right
        head_new = None  # before left

        # navigate on linked list
        counter: int = 1  # to compare element pos with left and right
        current = head
        while current:
            if counter >= left and counter <= right:
                new_node = ListNode(current.val, rev_mid)
                if not rev_mid:
                    tail = new_node
                rev_mid = new_node

            elif counter > right:
                tail.next = current
                break

            elif counter == left - 1:
                head_new = current

            current = current.next
            counter += 1

        if head_new:
            head_new.next = rev_mid
            return head
        return rev_mid  # rev_mid include reverse part + tail


# region linked list
# [1,2,3,4,5]
head = ListNode(1)
curr = head
for n in range(2, 6):
    curr.next = ListNode(n)
    curr = curr.next
# endregion

s = Solution()
result = s.reverseBetween(head, left=2, right=4)

while result:
    print(result.val, end=", ")
    result = result.next
