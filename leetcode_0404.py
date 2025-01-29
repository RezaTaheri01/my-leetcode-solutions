from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def walkthrough(node: Optional[TreeNode], isLeft: bool) -> int:
            if not node:
                return 0

            # If it's a left leaf, return its value
            if isLeft and not node.left and not node.right:
                return node.val

            # Sum of left and right subtrees
            return walkthrough(node.left, True) + walkthrough(node.right, False)

        return walkthrough(root, False)
