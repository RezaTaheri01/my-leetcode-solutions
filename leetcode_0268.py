class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = set(nums)
        
        num = 0
        while num in nums:
            num += 1
            
        return num