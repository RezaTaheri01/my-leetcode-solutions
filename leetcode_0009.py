class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)       
        pl, pr = 0, len(x_str) - 1
        
        while pl < pr:
            if x_str[pl] != x_str[pr]:
                return False
            pl += 1
            pr -= 1
        return True
    
    
s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(10101))
print(s.isPalindrome(16))