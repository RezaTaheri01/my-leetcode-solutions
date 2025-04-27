class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        counter = 0
        
        for index in range(1, len(nums) - 1):
            if (nums[index] / 2) == (nums[index - 1] + nums[index + 1]):
                counter += 1
                
        return counter
        
        
s = Solution()

print(s.countSubarrays([1,2,1,4,1]))
print(s.countSubarrays([1,1,1]))