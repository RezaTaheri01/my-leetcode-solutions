class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate_num = 0
        missing_num = 0

        # First loop: Identify the duplicate number by marking indices
        for num in nums:
            index = abs(num) - 1  # Map value to index
            if nums[index] < 0:
                duplicate_num = abs(num)  # Found the duplicate
            else:
                nums[index] *= -1  # Mark as visited

        # Second loop: Find the missing number
        for i in range(len(nums)):
            if nums[i] > 0:  # Unvisited index corresponds to missing number
                missing_num = i + 1
                break

        return [duplicate_num, missing_num]



s = Solution()
print(s.findErrorNums([2, 2, 3]))
