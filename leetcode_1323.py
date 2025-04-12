class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


s = Solution()

print(s.maximum69Number(9669))
print(s.maximum69Number(9999))
