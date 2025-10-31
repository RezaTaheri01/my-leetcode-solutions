from typing import List

# Space O(1), Time O(n log n)


class Solution0:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        for i, num in enumerate(nums[:-1]):
            if num == nums[i + 1]:
                result.append(num)
                if len(result) == 2:
                    break

        return result


# Space O(n), Time O(n)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] == 2:
                result.append(num)
                if len(result) == 2:
                    break

        return result
