class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Create a set of unique numbers in nums
        current_nums = set(nums)
        # Find numbers from 1 to n that are not in the set
        return [num for num in range(1, len(nums) + 1) if num not in current_nums]

    
# class Solution:
#     def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
#         # Mark each number's corresponding index as negative
#         for num in nums:
#             index = abs(num) - 1  # Get the index for this number
#             if nums[index] > 0:
#                 nums[index] = -nums[index]
        
#         # The positive values' indices are the missing numbers
#         return [i + 1 for i in range(len(nums)) if nums[i] > 0]
