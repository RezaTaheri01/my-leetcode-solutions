class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            n, r = divmod(n, 3)
            if r != 0 and r != 1:
                return False
        return True
    
    
s = Solution()

print(s.checkPowersOfThree(21))
