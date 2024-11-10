# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 0. get linked list1 as list
        li1: list = []
        while list1:
            li1.append(list1.val)
            list1 = list1.next

        # 1. get linked list2 as list
        li2: list = []
        while list2:
            li2.append(list2.val)
            list2 = list2.next

        # 2. merge two list
        li1.reverse()
        li2.reverse()
        result: list = []
        while li1 and li2:
            if li1[-1] < li2[-1]:
                result.append(li1.pop())
            else:
                result.append(li2.pop())

        tmp: list = li1 if li1 else li2

        while tmp:  # append remain of longer list
            result.append(tmp.pop())

        # 3.create linked list
        if result:
            head = ListNode(result[0])
            current = head
            for num in result[1:]:
                current.next = ListNode(num)
                current = current.next
        else:
            return list1

        # 4.return linked list
        return head


# Without lists
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # Initialize a dummy node to help with appending nodes in sorted order
#         dummy = ListNode()
#         current = dummy

#         # Merge nodes from list1 and list2 in sorted order
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next

#         # Attach remaining nodes, if any
#         if list1:
#             current.next = list1
#         elif list2:
#             current.next = list2

#         # Return the merged list, which starts from dummy's next
#         return dummy.next
