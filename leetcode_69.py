# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# we round it down to the nearest integer, 2 is returned.
class Solution:
    def mySqrt(self, x: int) -> int:
        # prev = float('inf')
        left, right = 1, x//2
        if x < 2:
            return x
        
        while left <= right:
            mid = (left + right) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
            else:
                right =  mid - 1

        return right
        
        