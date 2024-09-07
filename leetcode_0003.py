class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            char = s[end]

            if char in charDict and charDict[char] >= start:
                charDict[char] + 1

            charDict[char] = end

            max_len = max(max_len, end - start + 1)

        return max_len
