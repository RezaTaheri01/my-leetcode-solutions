class Solution:
    def scoreOfString(self, s: str) -> int:
        sums = 0
        prev = s[0]
        for char in s[1:]:
            sums += abs(ord(prev) - ord(char))
            prev = char

        return sums

        