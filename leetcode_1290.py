from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # get binary
        bin_str = ""
        while head:
            bin_str = str(head.val) + bin_str
            head = head.next

        # convert to decimal
        power = 0
        result = 0
        for b in bin_str:
            if b == "1":
                result += 2 ** power
            power += 1

        # return decimal
        return result
