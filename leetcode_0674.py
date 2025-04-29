from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                longest = max(longest, current_length)
                current_length = 1
                
        longest = max(longest, current_length)

        return longest


s = Solution()

print(s.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
print(s.findLengthOfLCIS(nums=[2, 2, 2]))
print(s.findLengthOfLCIS(nums=[1, 2, 3]))
print(s.findLengthOfLCIS(nums=[1]))
