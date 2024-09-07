class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        fix_nums = nums.copy()
        for ri, num in enumerate(nums):
            nums[ri] = fix_nums[ri - k]
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums
        
        
        
s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))