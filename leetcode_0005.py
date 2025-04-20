class Solution:
    def __init__(self):
        self.longest = ""
        self.longest_len = 0

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        self.longest = ""
        self.longest_len = 0

        def _longestPalindrome(pl: int, pr: int) -> str:
            while pl >= 0 and pr < l and s[pl] == s[pr]:
                if pr - pl + 1 > self.longest_len:
                    self.longest = s[pl:pr + 1]
                    self.longest_len = pr - pl + 1

                pl -= 1
                pr += 1

        for i in range(l):
            # odd
            _longestPalindrome(i, i)
            # even
            _longestPalindrome(i, i + 1)

        return self.longest


s = Solution()

print(s.longestPalindrome(s="babad"))
print(s.longestPalindrome(s="cbbd"))
print(s.longestPalindrome(s="c"))
