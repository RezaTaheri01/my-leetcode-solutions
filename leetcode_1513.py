class Solution:
    def numSub(self, s: str) -> int:
        mod = 1_000_000_007
        res = 0
        c = 0
        for char in s:
            if char == "1":
                c += 1
            else:
                res += c * (c + 1) // 2
                c = 0
                            
        res += c * (c + 1) // 2

        return res % mod


s = Solution()

print(s.numSub(s="0"))
print(s.numSub(s="1"))
print(s.numSub(s="0110111"))
print(s.numSub(s="1" * 10 ** 5))
