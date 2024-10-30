class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_pointer = 0
        write_pointer = 0

        while read_pointer < len(nums):
            if nums[read_pointer] != 0:
                nums[read_pointer], nums[write_pointer] = nums[write_pointer], nums[read_pointer]
                write_pointer += 1
            read_pointer += 1

        # return nums


s = Solution()
print(s.moveZeroes([0, 0, 1, 12, 7]))
