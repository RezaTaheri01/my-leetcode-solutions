class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result: list[str] = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


s = Solution()
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))
