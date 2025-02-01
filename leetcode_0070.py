class Solution:
    def __init__(self, *args, **kwargs):
        self.stairs_sequence: list = [1, 2]

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 0:
            n = abs(n)  # basement

        if len(self.stairs_sequence) >= n:
            return self.stairs_sequence[n-1]

        prev, current = self.stairs_sequence[-2], self.stairs_sequence[-1]
        for _ in range(n - 2):
            prev, current = current, current + prev
            self.stairs_sequence.append(current)

        return self.stairs_sequence[-1]


s = Solution()
print(s.climbStairs(n=8))


# Best of Code Readability
# class SolutionFib:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         current = 1
#         prev = 1
#         for i in range(n-1):
#             current, prev = current + prev, current
#         return current

# s = SolutionFib()
# print(s.climbStairs(7))
