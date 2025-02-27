from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        nodes = deque([root])
        depth: int = 1
        
        while nodes:
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if node:
                    if not node.left and not node.right:
                        return depth
                    nodes.append(node.left)
                    nodes.append(node.right)
                    
            depth += 1
            
        return depth