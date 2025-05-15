class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l = len(nums)
        # sum of its two sides is greater than the third side
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                if nums[j] + nums[j + 1] > nums[i]:
                    return nums[i] + nums[j] + nums[j + 1]
                else:
                    break

        return 0
