class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0
        
        for x in nums:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
    
s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
