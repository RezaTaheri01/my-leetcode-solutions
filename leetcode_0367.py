class Solution:  # Best
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                r = mid - 1
            else:
                l = mid + 1

        return False


# class Solution: # My first solution
#     def isPerfectSquare(self, num: int) -> bool:
#         if num == 1:
#             return True  # 1 is a perfect square

#         for div in range(2, int(num ** 0.5) + 1):
#             count = 0
#             while num % div == 0:
#                 count += 1
#                 num //= div
#             if count % 2 == 1:  # Odd exponent
#                 return False

#         return num == 1


s = Solution()
print(s.isPerfectSquare(5))
