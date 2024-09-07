def distinct_ways(n: int):
    if n == 0:
        return 1
    if n < 0:
        return 0

    total_ways = distinct_ways(n - 1) + distinct_ways(n - 2)
    return total_ways

def climbStairs(n: int) -> int:
    return distinct_ways(n)

print(climbStairs(35), end=', ')
    
# Best   
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
# print()
# print(s.climbStairs(7))