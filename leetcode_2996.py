class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        set_nums = set(nums)

        # find the longest prefix sequence
        start = nums[0]
        i = 0
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i + 1]:
                break
            i += 1

        # n * ((a1 + an)//2)
        sequence_sum = (i + 1) * (start + nums[i]) // 2

        # go through it one by one until it's not found on the list
        while sequence_sum in set_nums:
            sequence_sum += 1

        return sequence_sum


s = Solution()

# Test Cases
print(s.missingInteger([1, 2, 3, 2, 5]))  # 6
print(s.missingInteger([3, 4, 5, 1, 12, 14, 13]))  # 15
print(s.missingInteger([2, 1, 2, 3, 6, 7, 8, 9]))  # 4
print(s.missingInteger([4, 5, 6, 7, 8, 8, 9, 4, 3, 2, 7]))  # 30
