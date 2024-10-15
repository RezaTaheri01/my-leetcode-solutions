# class Solution: # Bad Solution
#     def addDigits(self, num: int) -> int:
#         digitSum = 10
#         while digitSum > 9:
#             digitSum = 0
#             for char in str(num):
#                 digitSum += int(char)
#             num = digitSum

#         return digitSum


class Solution:  # O(1) Solution
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9


s = Solution()
print(s.addDigits(26))
