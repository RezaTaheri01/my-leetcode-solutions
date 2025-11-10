from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = -nums[i]
                k -= 1
                if k == 0:
                    break
            else:
                break

        if k % 2 == 0:
            return sum(nums)

        return sum(nums) - 2 * (min(nums))


s = Solution()

print(s.largestSumAfterKNegations(nums=[4, 2, 3], k=1))
print(s.largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3))
print(s.largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2))
print(s.largestSumAfterKNegations(nums=[5, 6, 9, -3, 3], k=2))
