from typing import List
from collections import deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index: int = 0
        l: int = len(arr)
        queue = deque([])
        next_zero = False

        for index in range(l):
            if next_zero:
                next_zero = False
                queue.append(arr[index])
                arr[index] = 0
                continue

            if queue:
                temp = queue.popleft()
                queue.append(arr[index])
                arr[index] = temp

            if arr[index] == 0:
                next_zero = True

        print(arr)


s = Solution()

s.duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0])
s.duplicateZeros(arr=[1, 2, 3])
s.duplicateZeros(arr=[1])
s.duplicateZeros(arr=[0])
s.duplicateZeros(arr=[1, 0])
s.duplicateZeros(arr=[0, 1])
s.duplicateZeros(arr=[0, 1, 2, 3])


# [1,0,2,3,0,4,5,0] res = None
# [1,0,0,3,0,4,5,0] res = 2
# [1,0,0,2,0,4,5,0] res = 3
# [1,0,0,2,3,4,5,0] res = 0
# [1,0,0,2,3,0,5,0] res = 4
# [1,0,0,2,3,0,0,4] res = 4, 5
