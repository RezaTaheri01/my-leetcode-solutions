from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.k = k

        def navigate(node: Optional[TreeNode]):
            if not node or self.k == 0:
                return
            
            navigate(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            navigate(node.right)

        navigate(root)
        return self.result
