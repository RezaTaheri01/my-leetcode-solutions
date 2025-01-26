from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []  # List of lists of integers
        neighbors: deque[Optional[TreeNode]] = deque([root])

        while neighbors:
            level_size = len(neighbors)
            temp: List[int] = []
            for _ in range(level_size):
                current: Optional[TreeNode] = neighbors.popleft()
                if current:
                    temp.append(current.val)
                    if current.left:
                        neighbors.append(current.left)
                    if current.right:
                        neighbors.append(current.right)
            if temp:
                result.append(temp)

        return result
