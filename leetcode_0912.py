class Solution:
    def merge(self, nums, temp, left, mid, right):
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            nums[i] = temp[i]

    def mergeSort(self, nums, temp, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        self.mergeSort(nums, temp, left, mid)
        self.mergeSort(nums, temp, mid + 1, right)
        self.merge(nums, temp, left, mid, right)

    def sortArray(self, nums: list[int]) -> list[int]:
        temp = nums[:]
        self.mergeSort(nums, temp, 0, len(nums) - 1)
        return nums
