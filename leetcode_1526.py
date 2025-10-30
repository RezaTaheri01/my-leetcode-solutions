from typing import List
import numpy as np


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                ops += target[i] - target[i - 1]
        return ops


s = Solution()
print(s.minNumberOperations(target=[3, 1, 5, 4, 2]))  # 7
print(s.minNumberOperations(target=[3, 1, 1, 2]))  # 4
print(s.minNumberOperations(target=np.random.randint(low=1, high=10**5, size=99_000)))
