from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        n = len(nums)

        if n <= x:
            return [sum(nums)]

        if n < k:
            k = n

        counter = Counter(nums[:k])

        sub = sorted(counter.items(), key=lambda a: (-a[1], -a[0]))[:x]
        temp_sum = sum(num * count for num, count in sub)
        result.append(temp_sum)

        start_point = 0
        while start_point + k < n:
            left = nums[start_point]
            right = nums[start_point + k]
            counter[left] -= 1
            counter[right] = counter.get(right, 0) + 1

            sub = sorted(counter.items(), key=lambda a: (-a[1], -a[0]))[:x]
            temp_sum = sum(num * count for num, count in sub)
            result.append(temp_sum)

            start_point += 1

        return result



s = Solution()

print(s.findXSum(nums=[1,1,2,2,3,4,2,3], k=6, x=2))
print(s.findXSum(nums=[1,1,2,2,3,4,2,3], k=12, x=2))
print(s.findXSum([3,8,7,8,7,5], k = 2, x = 2))
print(s.findXSum([9, 5, 8], k = 2, x = 1))

import numpy as np
np.random.seed(42)
arr = np.random.randint(1, 50, size=(50,))
print(s.findXSum(arr , k = 2, x = 2)) # little bit slow

