# ab:cd
# if a == 0 then b < 10
# if a == 1 then b < 2
# c < 6 and d < 10

class Solution:
    def findLatestTime(self, s: str) -> str:
        a, b, _, c, d = s

        # Maximize hours
        if a == "?":
            a = "1" if b == "?" or int(b) < 2 else "0"
        if b == "?":
            b = "1" if a == "1" else "9"

        # Maximize minutes
        c = "5" if c == "?" else c
        d = "9" if d == "?" else d

        return f"{a}{b}:{c}{d}"


s = Solution()

print(s.findLatestTime("1?:?4"))
print(s.findLatestTime("0?:5?"))
print(s.findLatestTime("??:5?"))
print(s.findLatestTime("04:??"))
print(s.findLatestTime("?2:2?"))
