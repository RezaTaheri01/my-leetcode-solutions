class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors_sum = 0
        for div in range(1, int(num**0.5) + 1):
            if num % div == 0:
                divisors_sum += div
                if div != num // div:  # 28 / 2 = 14 so 24 / 14 = 2
                    divisors_sum += num // div
        return divisors_sum == num * 2


s = Solution()
print(s.checkPerfectNumber(28))
