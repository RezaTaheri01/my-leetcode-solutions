from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        subarray_len = -1

        start_indexes = []
        for i in range(n - 1, 0, -1):
            if nums[i] - nums[i - 1] == 1:
                if not start_indexes or start_indexes[-1] != i:
                    start_indexes.append(i - 1)

        i = 0
        for start in start_indexes[::-1]:
            if start >= i:
                c = 2
                odd = True
                for j in range(start + 2, n):
                    target = -1 if odd else 1
                    odd = not odd
                    
                    if nums[j] - nums[j - 1] == target:
                        c += 1
                    else:
                        break
                    
                    i = j
                    
                if c > subarray_len:
                    subarray_len = c

        return subarray_len


s = Solution()

print(s.alternatingSubarray(nums=[2, 3, 4, 3, 4]))  # 4
print(s.alternatingSubarray(nums=[4]))  # -1
print(s.alternatingSubarray(nums=[4, 5, 6]))  # 2
print(s.alternatingSubarray(nums=[4, 5, 4]))  # 3
print(s.alternatingSubarray(nums=[21, 9, 5]))  # -1
print(s.alternatingSubarray(nums=[1, 2, 2, 1, 2, 3]))  # 2
