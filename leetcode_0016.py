from typing import List

# You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = None
        closest_diff = float("inf")
        length = len(nums)

        # Sort the elements O(n log n)
        nums.sort()

        for i in range(length - 2):
            # now implement two curr_sum
            left, right = i + 1, length - 1  # Set left and right pointers

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - curr_sum)

                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = curr_sum

                if curr_sum > target:
                    right -= 1
                elif curr_sum == target:
                    return curr_sum
                else:
                    left += 1

        return closest_sum


s = Solution()

print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
print(s.threeSumClosest(nums=[0, 0, 0], target=1))
print(s.threeSumClosest(nums=[-1, -1, 2, 4], target=1))
print(s.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], target=-2))
print(s.threeSumClosest([1, 1, 1, 0], -100))
print(s.threeSumClosest([1, 1, 1, 0], 100))

