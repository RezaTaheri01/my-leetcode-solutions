class Solution:
    def maxSum(self, nums: list[int]) -> int:
        nums_set = set(nums)
        result = 0
        
        for num in nums_set:
            if num < 0:
                result += -num
                
        result += sum(nums_set)
        # result == 0 means all numbers are equal or lower that zero
        # so the maximum subarray is the number that closer to zero =>  max(nums_set)
        return max(nums_set) if result == 0 else result
    
    
s = Solution()

print(s.maxSum(nums = [1,2,3,4,5]))
print(s.maxSum(nums = [1,1,0,1,1]))
print(s.maxSum(nums = [1,2,-1,-2,1,0,-1]))
print(s.maxSum(nums = [-100, -20, -10]))
