class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        result = 0

        def _helper(pl, pr):
            counter = 0

            while pl >= 0 and pr < l and s[pl] == s[pr]:
                counter += 1
                pl -= 1
                pr += 1

            return counter

        for i in range(l):
            # odd
            result += _helper(i, i)
            # even
            result += _helper(i, i + 1)

        return result



s = Solution()

print(s.countSubstrings("a"))
print(s.countSubstrings("abc"))
print(s.countSubstrings("aba"))
print(s.countSubstrings("aaa"))
