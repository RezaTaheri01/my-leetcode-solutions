class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        rp = wp = c = 0
        prev = float('inf')
        while rp < len(nums):            
            if nums[rp] == prev:
                c += 1
            else:
                c = 0
                
            if c < 2:
                nums[wp] = nums[rp]
                wp += 1
                
            prev = nums[rp]
            rp += 1
        return wp
            
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        write_ptr = 2  # Start from the third element
        
        for read_ptr in range(2, len(nums)):
            if nums[read_ptr] != nums[write_ptr - 2]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
        
        return write_ptr


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
