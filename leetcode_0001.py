from typing import Counter


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count_map = Counter(nums)  # [1, 1, 1, 1] => {1 : 4}

        for num in nums:  # O(n)
            target_remain = target - num
            if target_remain in count_map:
                first_index = nums.index(num)

                if target_remain != num:
                    # two avoid duplicate index => [0, 0]
                    return [first_index, nums.index(target_remain, first_index)]
                elif count_map[num] > 1: # target_remain == num:
                    # index(value, start=first index, stop=last index)
                    return [first_index, nums.index(target_remain, first_index + 1)]


s = Solution()
print(s.twoSum([1, 1, 1, 1], 2))
