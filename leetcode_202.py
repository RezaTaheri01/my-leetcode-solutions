class Solution:
    def separate_pow(self, n: str):
        sqr_digits = [int(d) ** 2 for d in n]
        return sum(sqr_digits)

    def isHappy(self, n: int) -> bool:
        results = {}
        if n < 0 and n != int(n):
            return ValueError('Input is not positive integer')
        while n != 1:
            if n not in results:
                results[n] = True
            else:
                return False
            n = self.separate_pow(str(n))

        return True


s = Solution()
print(s.isHappy(2))
