from collections import deque
from typing import List, Optional

# reverse(): Use for in-place modification when we don’t need the original list
# List Slicing ([::-1]): Use to quickly create a reversed copy without modifying the original list
# reversed(): Ideal for creating an iterator to reverse without modifying the original list and if we need


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: list[int] = []
        neighbors: deque = deque([root])
        left_to_right: int = True

        while neighbors:
            level_size = len(neighbors)
            temp: list[int] = []
            for _ in range(level_size):
                current: TreeNode = neighbors.popleft()

                if current:
                    temp.append(current.val)
                    if current.left:
                        neighbors.append(current.left)
                    if current.right:
                        neighbors.append(current.right)
            if temp:
                if not left_to_right:
                    temp.reverse()
                result.append(temp)
                left_to_right = not left_to_right

        return result
