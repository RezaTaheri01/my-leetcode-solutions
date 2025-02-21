class Solution:
    def myAtoi(self, s: str) -> int:
        # remove any leading spaces
        s = s.strip()  
        if not s:
            return 0
        
        min_rng = -2 ** 31
        max_rng = 2 ** 31 - 1

        # Determine sign
        sign = 1
        index = 0
        if s[index] in "+-":
            sign = -1 if s[index] == "-" else 1
            index += 1

        result: int = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            if sign * result < min_rng:
                return min_rng
            if sign * result > max_rng:
                return max_rng
            index += 1

        return sign * result

s = Solution()
print(s.myAtoi('    -041 word hi'))  # -41
print(s.myAtoi('-042'))  # -42
print(s.myAtoi('42'))  # 42
print(s.myAtoi('0-1'))  # 0
print(s.myAtoi('words and 987'))  # 0
print(s.myAtoi('1337c0d3'))  # 1337
print(s.myAtoi(' -1123u3761867'))  # -1123
print(s.myAtoi('00000-42a1234'))  # 0
print(s.myAtoi('+-2'))  # 0
print(s.myAtoi('-115579378e25'))  # -115579378
print(s.myAtoi('1e5'))  # 1
print(s.myAtoi('+004500'))  # 4500
print(s.myAtoi('+ 0 123'))  # 0
print(s.myAtoi('4294967296'))  # 2147483647 (bigger than 2 ^ 31 - 1)
print(s.myAtoi('-4294967296'))  # -2147483648 (smaller than -2 ^ 31)
print(s.myAtoi('3.14159'))  # 3
print(s.myAtoi('  0000000000012345678'))  # 12345678
