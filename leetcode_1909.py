class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        counter = 0
        
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:  # Not strictly increasing
                counter += 1
                if counter > 1:
                    return False
                
                # Check if removal of nums[i] or nums[i+1] works
                if (i > 0 and nums[i - 1] >= nums[i + 1]) and (i + 2 < len(nums) and nums[i] >= nums[i + 2]):
                    return False

        return True



s = Solution()
print(s.canBeIncreasing(nums=[1, 2, 10, 11, 7])) # True
print(s.canBeIncreasing(nums=[1, 2, 10, 5, 7])) # True
print(s.canBeIncreasing(nums=[10, 2, 3, 5, 7])) # True
print(s.canBeIncreasing(nums=[2, 3, 1, 2])) # False 
print(s.canBeIncreasing(nums=[105, 924, 32, 968])) # True
