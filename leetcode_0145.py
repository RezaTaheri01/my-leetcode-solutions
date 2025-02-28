from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.results = []

        def navigate(node: Optional[TreeNode]):
            if not node:
                return

            navigate(node.left)
            navigate(node.right)
            self.results.append(node.val)

        navigate(root)

        return self.results
