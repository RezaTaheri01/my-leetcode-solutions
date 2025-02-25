from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.results: list[int] = []

        def navigate(node: Optional[TreeNode]) -> None:
            if not node:
                return

            navigate(node.left)
            self.results.append(node.val)
            navigate(node.right)

        navigate(root)
        return self.results
