# Todo: return sums directly
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.numbers: list[str] = []

        def navigate(node: Optional[TreeNode], current_value: str):
            if not node:
                return

            current_value += str(node.val)
            # current_value = current_value * 10 + node.val  # Construct number

            if not node.right and not node.left:
                self.numbers.append(current_value)
                return

            navigate(node.left, current_value)
            navigate(node.right, current_value)

        navigate(root, "")

        # add numbers
        result: int = 0
        for num in self.numbers:
            result += int(num)

        return result
