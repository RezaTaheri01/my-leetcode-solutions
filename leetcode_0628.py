import heapq


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        def heapify(nums: list[int], n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        # n = len(nums)

        # # Build a max heap
        # for i in range(n // 2 - 1, -1, -1):
        #     heapify(nums, n, i)

        # # Extract elements from the heap (just 3 maximums)
        # for i in range(n - 1, -1, -1):
        #     nums[i], nums[0] = nums[0], nums[i]
        #     heapify(nums, i, 0)

        # return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
        a = heapq.nlargest(3, nums)
        b = heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


s = Solution()
print(s.maximumProduct(nums=[5, 6, 2, 4, 8, 7, 0]))
print(s.maximumProduct(nums=[-100, -98, -1, 2, 3, 4]))
print(s.maximumProduct(nums=[1, 2, 3]))
print(s.maximumProduct(nums=[-1, -2, -3]))
print(s.maximumProduct(nums=[1, 2, 3, 4]))
print(s.maximumProduct(nums=[-8, -7, -2, 10, 20]))
