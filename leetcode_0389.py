class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts: dict = {}
        # count characters
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char in t:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                return char
