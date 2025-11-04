from typing import List


class Solution0:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        n = len(nums)

        # O(log n)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                result[0] = mid
                break

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # If target exist in nums
        if result[0] != -1:
            # O(log n) # Left
            left, right = 0, result[0]
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    if mid == 0:
                        result[0] = mid
                    right = mid - 1
                elif mid < (n - 1) and nums[mid] < target and nums[mid + 1] == target:
                    result[0] = mid + 1
                    break
                else:
                    left = mid + 1

            # O(log n) # Right
            left, right = result[0], n - 1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    if mid == n - 1:
                        result[1] = mid
                    left = mid + 1
                elif mid > 0 and nums[mid] > target and nums[mid - 1] == target:
                    result[1] = mid - 1
                    break
                else:
                    right = mid - 1

        return result


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        # O(log n) Left
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                index = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        result[0] = index

        # O(log n) Left
        if index != -1:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                if target == nums[mid]:
                    index = mid
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        result[1] = index

        return result


s = Solution()

print(s.searchRange(nums=[5, 7, 7, 8, 8, 8, 8, 10], target=8))  # [3, 6]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 8, 8, 10], target=5))  # [0, 0]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3, 4]
print(s.searchRange(nums=[5, 7, 7, 8, 10], target=8))  # [3, 3]
print(s.searchRange(nums=[5, 7, 7, 8, 10], target=10))  # [4, 4]
print(s.searchRange(nums=[5, 7, 7, 8, 10, 10], target=10))  # [4, 5]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1, -1]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=7))  # [1, 2]
print(s.searchRange(nums=[], target=0))  # [-1, -1]
print(s.searchRange(nums=[1, 1, 2], target=1))  # [0, 1]
print(s.searchRange([1], target=1))  # [0, 0]
