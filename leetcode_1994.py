from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        if k == 1:
            return 0

        k -= 1

        minimum = nums[-1]
        for i in range(len(nums) - k):
            minimum = min(abs(nums[i] - nums[i + k]), minimum)

        return minimum


s = Solution()

print(s.minimumDifference(nums=[90], k=1))
print(s.minimumDifference(nums=[90, 1], k=1))
print(s.minimumDifference(nums=[90, 1], k=2))
print(s.minimumDifference(nums=[9, 4, 1, 7], k=2))  # 1, 4, 7, 9
