from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wi = 1
        prev = nums[0]
        for num in nums[1:]:
            if num != prev:
                nums[wi] = num
                wi += 1
            prev = num

        return wi


s = Solution()


print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates(nums=[1, 1, 2]))
print(s.removeDuplicates(nums=[1, 1, 1]))
print(s.removeDuplicates(nums=[1, 2, 3, 4, 5]))
