class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1  
            else:
                right = mid
                
        return nums[right]
            
            

s = Solution()

print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 9, 10, 11, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
print(s.findMin([13, 14, 15, 1]))
print(s.findMin([2, 3, 4, 5, 1]))
print(s.findMin([0]))
print(s.findMin([3, 1, 2]))
print(s.findMin([19, 20, 5, 15, 16, 17, 18]))
