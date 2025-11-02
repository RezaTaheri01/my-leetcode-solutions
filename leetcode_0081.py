from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search_rotated(sp, ep) -> bool:
            if sp > ep:
                return False

            mid = (sp + ep) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[sp] == nums[mid] == nums[ep]:
                return binary_search_rotated(sp + 1, ep - 1)

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
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
print(s.search(nums=[5, 5, 6, 0, 0, 1, 2, 2, 2, 2, 4], target=4))
print(s.search(nums=[1, 1, 1, 2, 1, 1], target=2))
print(s.search(nums=[1, 0, 1, 1, 1], target=0))
print(s.search(nums=[1, 1, 1, 0, 1], target=0))
