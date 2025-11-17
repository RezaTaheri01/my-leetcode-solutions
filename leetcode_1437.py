from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 in nums:
            prev_idx = nums.index(1)
        else:
            return True

        for i in range(prev_idx + 1, len(nums)):
            if nums[i] == 1:
                if i - prev_idx - 1 < k:
                    return False
                prev_idx = i

        return True


s = Solution()

print(s.kLengthApart([1, 0, 1], 2))
