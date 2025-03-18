from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)

        for i, digit in enumerate(num):
            count = str(counts.get(str(i), 0))
            if count != digit:
                return False
        return True


s = Solution()

print(s.digitCount("1210"))
