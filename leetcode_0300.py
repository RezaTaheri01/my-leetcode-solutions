# Todo: binary search with patience sorting

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:        
        n = len(nums)
        dp = [1] * n
        result: int = 1
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    result = max(dp[i], result)
            
        
                    
        return result
    
    
    
s = Solution()

print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([7,7,7,7,7,7,7]))
print(s.lengthOfLIS([2, 5, 3, 7]))
