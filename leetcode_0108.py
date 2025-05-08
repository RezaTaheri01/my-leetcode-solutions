from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.head = None

        def buildTree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:  # Base case: no elements in this range
                return None

            mid = (left + right) // 2  # Middle index
            node = TreeNode(val=nums[mid])  # Create the root node
            if not self.head:
                self.head = node

            # Recursively build left and right subtrees
            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)

            return node

        buildTree(0, len(nums) - 1)
        return self.head
