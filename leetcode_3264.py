import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pairs: list[list[int]] = []

        # create pairs (if values are equals => compare indexes)
        for i in range(len(nums)):  # O(n)
            pairs.append([nums[i], i])

        for _ in range(k):  # O(k)
            heapq.heapify(pairs)
            pairs[0][0] = pairs[0][0] * multiplier

        for val, i in pairs:  # O(n)
            nums[i] = val

        return nums


s = Solution()
print(s.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
