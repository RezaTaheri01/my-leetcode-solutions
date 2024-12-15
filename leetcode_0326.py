class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1

# class Solution: # O(1)
#     def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and 3 ** 19 % n == 0  # 2^31 ~= 3^19


s = Solution()
print(s.isPowerOfThree(387420489))
