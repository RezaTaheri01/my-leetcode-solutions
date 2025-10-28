from typing import List

# 4Sum: Pick one number => 3Sum for rest => Pick one number => 2Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        n = len(nums)

        for j in range(n - 3):
            # Skip duplicates for the first number
            if j > 0 and nums[j] == nums[j - 1]:
                continue

            for i in range(j + 1, n - 2):
                # Skip duplicates for the second number
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue

                l, r = i + 1, n - 1
                while l < r:
                    curr_sum = nums[j] + nums[i] + nums[l] + nums[r]
                    if curr_sum == target:
                        results.append([nums[j], nums[i], nums[l], nums[r]])

                        # Skip duplicates for third and fourth numbers
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1

        return results


s = Solution()

print(s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(s.fourSum(nums=[2, 2, 2, 2, 2, 1, 1, 1, 3, 5], target=8))
print(s.fourSum(nums=[2, 2, 2, 2, 2, 1, 1, 1, 3, 5, 0, 0, 0, 8], target=8))
print(s.fourSum(nums=[2, 2, 2, 2, 2], target=8))
print(s.fourSum(nums=[1000000000, 1000000000, 1000000000, 1000000000], target=-294967296))
