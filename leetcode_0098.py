from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        return (self.isValidBST(root.left, min_val, root.val) and
                self.isValidBST(root.right, root.val, max_val))


s = Solution()


#   2
#  / \
# 1   3
head = TreeNode(2)
left_temp = head
right_temp = head

left_temp.left = TreeNode(1)
right_temp.right = TreeNode(3)

left_temp = left_temp.left
right_temp = right_temp.right
print(s.isValidBST(head))  # True

#   5
#  / \
# 1   6
#    / \
#   3   7
head = TreeNode(5)
left_temp = head
right_temp = head

left_temp.left = TreeNode(1)
right_temp.right = TreeNode(6)

left_temp = left_temp.left
right_temp = right_temp.right

right_temp.left = TreeNode(3)
right_temp.right = TreeNode(7)
print(s.isValidBST(head))  # True
