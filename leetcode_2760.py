from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, r = 0, 0

        def recursive(curr_idx, prev_val) -> int:
            if curr_idx >= len(nums) or (nums[curr_idx] > threshold):
                return curr_idx

            if nums[curr_idx] % 2 != prev_val % 2:
                return recursive(curr_idx + 1, nums[curr_idx])

            return curr_idx

        j = 0
        while j < len(nums):
            if nums[j] % 2 == 0 and nums[j] <= threshold:
                r_new = recursive(j + 1, nums[j])

                if r_new - j > r - l:
                    r = r_new
                    l = j

                j = r_new
            else:
                j += 1

        return r - l


s = Solution()

print(s.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5)) # 3
print(s.longestAlternatingSubarray(nums=[1, 2], threshold=2)) # 1
print(s.longestAlternatingSubarray(nums=[2, 1], threshold=2)) # 2
print(s.longestAlternatingSubarray(nums=[2, 3, 4, 5], threshold=4)) # 3
print(s.longestAlternatingSubarray(nums=[4], threshold=4)) # 1
print(s.longestAlternatingSubarray(nums=[4], threshold=5)) # 1
print(s.longestAlternatingSubarray(nums=[4], threshold=3)) # 0
print(s.longestAlternatingSubarray(nums=[2, 3, 3, 10], threshold=3))  # 2
print(s.longestAlternatingSubarray(nums=[2, 3, 3, 10], threshold=10))  # 2
print(s.longestAlternatingSubarray(nums=[1, 6], threshold=2))  # 0
print(s.longestAlternatingSubarray(nums=[2, 5], threshold=2))  # 1
print(s.longestAlternatingSubarray(nums=[10, 1, 10], threshold=3))  # 0
