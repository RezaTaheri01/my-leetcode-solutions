class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + self.trailingZeroes(n//5) if n else 0
    
    
    
s = Solution()

print(s.trailingZeroes(0)) # 0
print(s.trailingZeroes(3)) # 0
print(s.trailingZeroes(5)) # 1
print(s.trailingZeroes(10)) # 2
print(s.trailingZeroes(15)) # 3
print(s.trailingZeroes(30)) # 7
print(s.trailingZeroes(40)) # 9
print(s.trailingZeroes(50)) # 12
print(s.trailingZeroes(65)) # 15
print(s.trailingZeroes(75)) # 18
print(s.trailingZeroes(200)) # 49
