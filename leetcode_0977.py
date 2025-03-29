from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        write_index = len(nums) - 1
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[write_index] = nums[left] ** 2
                left += 1
            else:
                result[write_index] = nums[right] ** 2
                right -= 1
                
            write_index -= 1
        
        return result
                    
        
        

s = Solution()

print(s.sortedSquares(nums = [-4,-1,0,3,10]))
print(s.sortedSquares(nums = [-7,-3,2,3,11]))
print(s.sortedSquares(nums = [-7]))

