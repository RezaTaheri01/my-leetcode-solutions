class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + n)

        return rob2


s = Solution()

print(s.rob(nums=[1, 2, 3, 1]))
print(s.rob(nums=[2, 7, 9, 3, 1]))
print(s.rob(nums=[2, 1, 1, 2]))
