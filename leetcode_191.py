class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <= 0:
            return 0
        binary = bin(n)[2:]
        return binary.count('1')


s = Solution()
print(s.hammingWeight(12))

n = 12
print(bin(12))
print(bin(n << 1)) # add 1 bit
print(bin(n >> 1)) # remove 1 bit
