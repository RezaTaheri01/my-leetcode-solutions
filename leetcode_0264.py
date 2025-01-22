# https://www.geeksforgeeks.org/ugly-numbers/
# sequence to three groups as below:
#      (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
#      (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
#      (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly: list[int] = [0] * n  # To store ugly numbers

        # 1 is the first ugly number
        ugly[0] = 1

        # i2, i3, i5 will indicate indices for
        # 2,3,5 respectively
        i2 = i3 = i5 = 0

        # Set initial multiple value
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for l in range(1, n):
            ugly[l] = min(next_multiple_of_2,
                          next_multiple_of_3,
                          next_multiple_of_5)
            
            # Increment the value of index accordingly
            if ugly[l] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
    
            if ugly[l] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
    
            if ugly[l] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        return ugly[-1]


s = Solution()


print(s.nthUglyNumber(20))
print(s.nthUglyNumber(1))
