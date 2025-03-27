class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))

        

s = Solution()

print(s.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
print(s.heightChecker(heights=[5, 1, 2, 3, 6]))
print(s.heightChecker(heights=[1, 2, 3, 1, 3]))
print(s.heightChecker(heights=[1, -1, 2, -5]))
