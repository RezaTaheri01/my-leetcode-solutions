class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0
        start = 0  # Start of the sliding window

        for end in range(len(s)): # O(n)
            char = s[end]

            if char in char_dict and char_dict[char] >= start:
                # Move start pointer to the right of the previous occurrence of char
                start = char_dict[char] + 1

            # Update the latest index of the character
            char_dict[char] = end

            # Calculate the max length of the substring
            max_len = max(max_len, end - start + 1)

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
