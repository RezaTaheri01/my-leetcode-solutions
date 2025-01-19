class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1, 3, 6, 10, 15, 21, ...

        # x^2 + x - 2n = 0
        delta: int = 1 + 4*2*n 
        
        if delta < 0:
            return 0
        return int((-1 + delta ** 0.5) / 2)
    
    
s = Solution()

print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
