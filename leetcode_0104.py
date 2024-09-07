# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The depth of the current node is 1 plus the maximum of the depths of its subtrees
        return max(left_depth, right_depth) + 1





# Create the root node
root = TreeNode(1)

# Add left and right children to the root node
root.left = TreeNode(2)
root.right = TreeNode(3)

# Add children to the left child of the root
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Add children to the right child of the root
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(root))
