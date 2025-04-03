class Solution:
    def isGood(self, nums: list[int]) -> bool:
        l = len(nums)
        nums.sort()

        if nums[-1] != l - 1:
            return False

        for i in range(l - 1):
            if nums[i] != i + 1:
                return False

        return True
