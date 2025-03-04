from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0    
        def navigate(node: Optional[TreeNode]):
            if not node:
                return
            
            value = node.val
            if value >= low and value <= high:
                self.sum += value  
                            
            if value >= low:             
                navigate(node.left)
            if value <= high:
                navigate(node.right)
                
        navigate(root)
        return self.sum
