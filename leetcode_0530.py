from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum = float("inf")
        self.numbers = []

        def navigate(node):  # O(n)
            if not node:
                return
            self.numbers.append(node.val)
            navigate(node.left)
            navigate(node.right)

        # get all tree values and append to numbers list
        navigate(root)

        # sort numbers list
        sorted_nums = sorted(self.numbers)  # O(n log n)
        prev = sorted_nums[0]

        # check difference two by two and side by side and compare with current minimum
        for num in sorted_nums[1:]:  # O(n)
            minimum = min(minimum, abs(prev - num))
            if minimum == 0:  # zero is minimum
                break
            prev = num

        return minimum
