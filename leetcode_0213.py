from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(start, end):
            rob1, rob2 = 0, 0

            for n in nums[start:end]:
                rob1, rob2 = rob2, max(rob2, rob1 + n)

            return rob2

        return max(nums[0], _rob(1, len(nums)), _rob(0, len(nums) - 1))
