from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = [0] * (n + 1)
        left, right = 0, n

        for i, char in enumerate(s):
            if char == "I":
                result[i] = left
                left += 1
            else:
                result[i] = right
                right -= 1

        result[-1] = left  # left and right are equal to each other at this point

        return result


s = Solution()

print(s.diStringMatch(s="IDID"))
print(s.diStringMatch(s="III"))
print(s.diStringMatch(s="DDI"))
print(s.diStringMatch(s="I"))
print(s.diStringMatch(s="D"))
