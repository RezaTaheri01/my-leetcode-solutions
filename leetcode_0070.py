class Solution:
    def __init__(self):
        self.stairs_sequence: list = [1, 2]  # Base cases

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 1  # There is 1 way to stay at the ground (by doing nothing)

        if len(self.stairs_sequence) >= n:
            return self.stairs_sequence[n - 1]

        prev, current = self.stairs_sequence[-2], self.stairs_sequence[-1]
        for _ in range(len(self.stairs_sequence), n):
            prev, current = current, prev + current
            self.stairs_sequence.append(current)

        return self.stairs_sequence[n - 1]


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
