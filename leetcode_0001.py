from typing import Counter


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count_map = Counter(nums)
        for num in nums:
            tmp = target - num
            if num < target and tmp in count_map:
                if (tmp == num and count_map[num] > 1):
                    one = nums.index(num)
                    nums[one] = num + 1 # change the first number to find the index of second 
                    return [one, nums.index(tmp)]
                elif tmp != num:
                    return [nums.index(num), nums.index(tmp)]


s = Solution()
print(s.twoSum([1,1,1,1], 2))
