class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Count occurrences of red(0), white(1), blue(2)
        color_counts = [0] * 3
        
        # Count each color
        for num in nums:
            color_counts[num] += 1
        
        # Rewrite array in sorted order
        current_index = 0
        for color in range(3):
            for _ in range(color_counts[color]):
                nums[current_index] = color
                current_index += 1
                
        print(nums)


s = Solution()

s.sortColors([2, 0, 2, 1, 1, 0])
