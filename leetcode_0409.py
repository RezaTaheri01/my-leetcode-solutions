from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest: int = 0

        counts = Counter(s)
        # for char in s:
        #     counts[char] = counts.get(char, 0) + 1

        plus_one = False
        for val in counts.values():
            if val % 2 == 0:
                longest += val
            else:
                longest += val - 1
                plus_one = True

        return longest + 1 if plus_one else longest
