from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # n = len(nums)
        # nums.sort()  
           
        # l = 0
        # r = n - 1
        # while l <= r:
        #     mid = (l + r) // 2
            
        #     if nums[mid] == original:
        #         original *= 2
        #         l, r = mid, n - 1
                
        #     elif nums[mid] > original:
        #         r = mid - 1
                
        #     else:
        #         l = mid + 1
                
        # return original
        
        nums = set(nums)
        while original in nums:
            original *= 2
            
        return original
    


s = Solution()

print(s.findFinalValue(nums = [5,3,6,1,12], original = 3))
print(s.findFinalValue(nums = [2,7,9], original = 4))
print(s.findFinalValue(nums = [2], original = 2))
print(s.findFinalValue(nums = [2], original = 6))
print(s.findFinalValue(nums = [], original = 6))
print(s.findFinalValue(nums = [1, 2, 4, 8, 16, 32], original = 1))
