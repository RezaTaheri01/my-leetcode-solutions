from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.results = []

        def navigate(node: Optional[TreeNode]):
            if not node:
                return
            
            self.results.append(node.val)
            navigate(node.left)
            navigate(node.right)

        navigate(root)

        return self.results
