class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        c: int = 0
        n: int = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c += 1
        return c


s = Solution()
print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
