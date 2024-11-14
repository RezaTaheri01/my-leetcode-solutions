from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def navigate(rightSide: Optional[TreeNode], leftSide: Optional[TreeNode]):
            # check sizes
            if not rightSide and not leftSide:
                return True
            if not rightSide or not leftSide:
                return False
            # check values
            if rightSide.val != leftSide.val:
                return False

            return (navigate(rightSide.left, leftSide.right) and
                    navigate(rightSide.right, leftSide.left))

        return navigate(root.right, root.left)
