from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def navigate(mamaNode, leftNode, rightNode):  # M
            if not leftNode and not rightNode:     # /     \
                return                            # L       R

            mamaNode.right = leftNode
            mamaNode.left = rightNode

            if leftNode:
                navigate(leftNode, leftNode.left, leftNode.right)
            if rightNode:
                navigate(rightNode, rightNode.left, rightNode.right)

        if not root:
            return root

        navigate(root, root.left, root.right)

        return root
