from typing import List
import heapq


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = list(enumerate(nums))

        # get k largest elements base on nums
        largest_k = heapq.nlargest(k, indexed_nums, key=lambda x: x[1])

        # sorted base on indexes
        largest_k.sort(key=lambda x: x[0])

        return [num for _, num in largest_k]


s = Solution()

print(s.maxSubsequence(nums=[1, 3, 2, 3], k=3))
print(s.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
print(s.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(s.maxSubsequence(nums=[3, 4, 3, 3], k=2))
print(s.maxSubsequence(nums=[50, -75], k=2))
print(s.maxSubsequence(nums=[-1], k=1))
