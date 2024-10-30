class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        length = len(height)
        p_left, p_right = 0, length - 1

        while p_left < p_right:
            container = min(
                height[p_left], height[p_right]) * (p_right - p_left)

            if maximum < container:
                maximum = container
                
            if height[p_left] < height[p_right]:
                p_left += 1
            else:
                p_right -= 1   
                
        return maximum 




s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))