class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:  # O(log n)
            n /= 2

        return n == 1

    def isPowerOfTwoO1(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0  # O(1)

#    1000  (which is 8)  |    1010  (which is 10)
#  & 0111  (which is 7)  |  & 1001  (which is 9)
#  --------              |  --------
#    0000                |    1000

s = Solution()
print(s.isPowerOfTwo(16))
