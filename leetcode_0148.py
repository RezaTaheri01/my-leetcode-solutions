# Todo: sort linked list not list(merge sort & quick sort)
from typing import Optional
from random import randint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def linkedListToList(self, curr: ListNode) -> list[int]:
        result: list[int] = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def updateLinkedList(self, curr: ListNode, sorted_list: list[int]) -> None:
        for num in sorted_list:
            if curr:
                curr.val = num
                curr = curr.next

    def quick_sort(self, arr: list[int]):
        length = len(arr)

        # base case
        if length < 2:
            return arr

        # select a pivot
        pivot_index = randint(0, length - 1)
        pivot = arr[pivot_index]

        # define right and left lists
        left: list[int] = []
        right: list[int] = []

        # find all values greater or equal and smaller than pivot
        for num in arr[:pivot_index] + arr[pivot_index + 1:]:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)

        return (self.quick_sort(left)) + [pivot] + self.quick_sort(right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers: list[int] = self.linkedListToList(head)

        # numbers = self.quick_sort(numbers)
        numbers.sort()

        self.updateLinkedList(head, numbers)

        return head


def create_linked_list(numbers: list[int]):
    head = ListNode(numbers[0])
    curr = head
    for num in numbers[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


s = Solution()
print(s.sortList(create_linked_list([4, 2, 1, 3])))
