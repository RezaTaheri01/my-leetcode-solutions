from typing import List
import bisect


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return left

            mid = (left + right) // 2

            if mid >= len(nums):
                return len(nums)

            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

            return binary_search(left, right)

        n = len(nums)

        index = binary_search(0, n)
        negatives = bisect.bisect_left(nums, 0)

        return max(negatives, n - index)


s = Solution()

print(s.maximumCount(nums=[-2, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]))
print(s.maximumCount(nums=[5, 20, 66, 1314]))
print(s.maximumCount(nums=[-1314, -66, -20, -5]))
print(s.maximumCount(nums=[5]))
print(s.maximumCount(nums=[-5]))
