from typing import Counter
# You may assume that each input would have exactly one solution!

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count_map = Counter(nums)  # [1, 1, 1, 1] => {1 : 4}

        for num in nums:  # O(n)
            target_remain = target - num
            if target_remain in count_map:
                first_index = nums.index(num)
                if target_remain != num:
                    # index(value, start=first index, stop=last index)
                    return [first_index, nums.index(target_remain, first_index)]
                elif count_map[num] > 1: # target_remain == num:
                    # (first_index + 1) to avoid duplicate index like => [0, 0]
                    return [first_index, nums.index(target_remain, first_index + 1)]


s = Solution()
print(s.twoSum([2, 7, 11, 15, 2], 9))  # Expected output: [0, 1]
print(s.twoSum([1, 3, 3, 2], 6))  # Expected output: [1, 2] (3 and 3 from indices 1 and 2)
print(s.twoSum([-3, 4, 3, 90], 0))  # Expected output: [0, 2] (-3 + 3 = 0)
print(s.twoSum([2, 2, 2, 2], 4))  # Expected output: [0, 1]
print(s.twoSum([3, 2, 4], 6))  # Expected output: [1, 2] (2 and 4 make 6)

