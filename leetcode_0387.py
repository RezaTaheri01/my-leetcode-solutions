class Solution:  # O(2n) => O(n)
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        # count s
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        c = 0
        for key, value in counts.items():  # O(n)
            if value == 1:
                return s.index(key)
            c += 1

        return -1
