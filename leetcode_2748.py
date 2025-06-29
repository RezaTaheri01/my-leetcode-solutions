import math

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    counter += 1

        return counter
