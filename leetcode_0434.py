class Solution:
    def countSegments(self, s: str) -> int:
        # return len(s.split())
        s = s.strip()
        if not s:
            return 0

        prev = None
        c = 0
        for char in s:
            if char == " " and prev != char:
                c += 1
            prev = char

        return c + 1


s = Solution()
print(s.countSegments(""))
print(s.countSegments(s="Hello, my name is John"))
print(s.countSegments(s="Hello"))
