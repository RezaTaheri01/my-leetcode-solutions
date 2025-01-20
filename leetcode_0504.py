class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        base: int = 7
        result: str = ""
        is_negative : bool = num < 0
        num = abs(num)

        while num > 0:
            remain = num % base
            num //= base

            result = str(remain) + result

        return "-" + result if is_negative  else result


s = Solution()
print(s.convertToBase7(-7))
print(s.convertToBase7(100))
print(s.convertToBase7(0))
