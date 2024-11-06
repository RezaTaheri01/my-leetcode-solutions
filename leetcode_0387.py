class Solution:  # O(2n) => O(n)
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        # count s
        for char in s:  # O(n)
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        c = 0
        for key, value in counts.items():  # O(n)
            if value == 1:
                return s.index(key)
            c += 1

        return -1
