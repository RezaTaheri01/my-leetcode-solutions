# Todo: Bits manipulation
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # O(n) and constant space
        visited: dict = {num: False for num in nums}

        for num in (nums):  # O(n)
            visited[num] = not visited[num]

        # O(n)
        return [key for key, value in visited.items() if value]


s = Solution()

print(s.singleNumber(nums=[1, 2, 1, 3, 2, 5]))
print(s.singleNumber(nums=[-1, 0]))
print(s.singleNumber(nums=[1, 0]))
print(s.singleNumber(nums=[]))
