class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def isPrime(number: int):
            # A prime number is a positive integer greater than one that is only divisible by itself and one.
            if number <= 1:
                return False
            for div in range(2, int(number ** 0.5) + 1):
                if number % div == 0:
                    return False
            return True

        d = 2
        while d < n + 1:
            while n % d == 0:
                n //= d
            if d > 6 and d % 2 == 1 and isPrime(d):
                return False
            d += 1
        return True


s = Solution()
print(s.isUgly(120))  # => 2,60 => 2,30 => 2,15 => 3,5 => 5
print(s.isUgly(905391974))

