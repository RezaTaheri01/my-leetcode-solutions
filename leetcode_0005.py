# Todo: Improve time complexity

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(start, end) -> bool:
            pl, pr = start, end

            while pl < pr:
                if s[pl] != s[pr]:
                    return False
                pl += 1
                pr -= 1
            return True

        l = len(s)
        for i in range(l-1, -1, -1):
            start = 0
            while start + i < l:
                if isPalindrome(start, start + i):
                    return s[start: start + i + 1]
                start += 1



s = Solution()

print(s.longestPalindrome(s = "babad"))
print(s.longestPalindrome(s = "cbbd"))