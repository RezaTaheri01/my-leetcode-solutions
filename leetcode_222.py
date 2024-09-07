# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self, *args, **kwargs):
        self.counter = 0

    def nodes(self, root: Optional[TreeNode]) -> None:
        if root and root.val != None:
            self.counter += 1
        else:
            return

        self.nodes(root.left)
        self.nodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.nodes(root)
        return self.counter


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
print(s.countNodes(root))
