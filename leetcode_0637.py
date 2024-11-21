from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def navigate(self, node, total):
        # If we reach a leaf node, check if the total equals the target
        if not node:
            return False
        total += node.val
        if not node.left and not node.right:  # Leaf node
            return total == self.target

        # Recursively check left and right subtrees
        return self.navigate(node.left, total) or self.navigate(node.right, total)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        return self.navigate(root, 0)  # Start with 0 as the initial sum
