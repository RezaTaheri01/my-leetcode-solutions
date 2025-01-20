class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map: dict = {"0": 0, "1": 1, "2": 2, "3": 3,
                           "4": 4, "5": 5, "6": 6, "7": 7,
                           "8": 8, "9": 9}

        if len(num1) < len(num2):  # num1 should be greater or equal to num2
            num1, num2 = num2, num1

        result: int = 0
        tens_d2: int = 1

        for d2 in num2[::-1]:
            tens_d1 = 1
            for d1 in num1[::-1]:
                # multiply digits with their place value
                temp = (digit_map[d2] * digit_map[d1]) * tens_d1 * tens_d2
                result += temp
                tens_d1 *= 10
            tens_d2 *= 10

        return str(result)



s = Solution()

print(s.multiply("2", "3"))
print(s.multiply("123", "56"))
print(s.multiply("123", "456"))
