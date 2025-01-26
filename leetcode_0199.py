from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []
        neighbors: deque = deque([root])

        while neighbors:
            level_size = len(neighbors)
            temp = -101 # -100 <= Node.val <= 100
            for _ in range(level_size):
                current: TreeNode = neighbors.popleft()

                if current:
                    temp = current.val
                    if current.left:
                        neighbors.append(current.left)
                    if current.right:
                        neighbors.append(current.right)
            if temp != -101:
                result.append(temp)

        return result
