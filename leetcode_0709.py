class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ""

        for char in s:
            ord_temp = ord(char)
            if 65 <= ord_temp <= 90:
                new_s += chr(ord_temp + 32)
            else:
                new_s += char

        return new_s


s = Solution()

print(s.toLowerCase("Hello"))
