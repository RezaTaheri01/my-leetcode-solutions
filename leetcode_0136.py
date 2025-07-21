from typing import List

# a ^ a = 0 → a number XORed with itself is 0
# a ^ 0 = a → a number XORed with 0 is the number itself
# [2, 2, 3, 2]
# 2 ^ 2 = 10 ^ 10 = 00 → 0
# 0 ^ 3 = 00 ^ 11 = 11 → 3
# 3 ^ 2 = 11 ^ 10 = 01 → 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        result = nums[0]

        for num in nums[1:]:
            result ^= num

        return result
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for num in nums[1:]:
            result ^= num

        return result