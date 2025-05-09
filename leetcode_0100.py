from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def navigate(node_p, node_q) -> bool:
            if not node_p and not node_q:
                return True

            if (not node_p or not node_q) or (node_p.val != node_q.val) or \
                not navigate(node_p.left, node_q.left):
                return False

            return navigate(node_p.right, node_q.right)

        return navigate(p, q)
