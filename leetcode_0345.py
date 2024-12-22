class Solution:
    def reverseVowels(self, s: str) -> str:
        chars: list[str] = list(s)  # Preserve original characters
        vowels: str = "aeiouAEIOU"  # Include uppercase vowels

        l, r = 0, len(s) - 1
        while l < r:
            if chars[l] in vowels:  # Check vowels in original case
                while l < r and chars[r] not in vowels:
                    r -= 1
                if l < r:
                    chars[l], chars[r] = chars[r], chars[l]
                    r -= 1
            l += 1

        return "".join(chars)


s = Solution()
print(s.reverseVowels("hello"))         # Output: "holle"
print(s.reverseVowels("leet_code"))      # Output: "leot_cede"
print(s.reverseVowels("aA"))            # Output: "Aa"
