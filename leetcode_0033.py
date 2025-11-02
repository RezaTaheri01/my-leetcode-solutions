
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search_rotated(sp, ep) -> int:
            if sp > ep:
                return -1

            mid = (sp + ep) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[ep]:  # Left half is sorted
                if nums[sp] <= target < nums[mid]:
                    ep = mid - 1
                else:
                    sp = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[ep]:
                    sp = mid + 1
                else:
                    ep = mid - 1

            return binary_search_rotated(sp, ep)

        return binary_search_rotated(0, len(nums) - 1)


s = Solution()

print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(s.search(nums=[3, 4, 5, 6, 7, 1, 2], target=3))  # 0
print(s.search(nums=[3, 4, 5, 6, 7, 1, 2], target=2))  # 6
print(s.search(nums=[2, 5, 6, 0, 1, 2], target=0))  # 3
print(s.search(nums=[3, 5, 6, 0, 1, 2], target=3))  # 0
print(s.search(nums=[3, 4, 5, 6, 7, 1], target=7))  # 4
print(s.search(nums=[3, 4, 5, 6, 7, 1], target=1))  # 5
print(s.search(nums=[3, 4, 5, 6, 7, 1], target=6))  # 3
print(s.search(nums=[3, 4, 5, 6, 7, 1], target=5))  # 2
print(s.search(nums=[3, 4, 5, 6, 7, 1], target=4))  # 1
print(s.search(nums=[5, 6, 0, 1, 2, 4], target=5))  # 0
print(s.search(nums=[1, 2, 4, 0], target=4))  # 2
