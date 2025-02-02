class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]


        dp_table = [0] * n
        dp_table[0] = nums[0]
        dp_table[1] = max(nums[0], nums[1]) 
        
        for i in range(2, n):
            dp_table[i] = max(dp_table[i - 1], nums[i] + dp_table[i - 2])
        
        return dp_table[-1]  # Return the last element which is the result for all houses
        

s = Solution()

print(s.rob(nums = [1,2,3,1]))
print(s.rob(nums = [2,7,9,3,1]))
print(s.rob(nums = [2,1,1,2]))
