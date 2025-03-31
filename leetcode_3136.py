class Solution:
    def isValid(self, word: str) -> bool:
        vowels: set = {'a', 'e', 'i', 'o', 'u'}

        # It contains a minimum of 3 characters.
        if len(word) < 3:
            return False

        oneVowel = False
        oneConsonant = False
        for char in word:
            # It contains only digits (0-9), and English letters (uppercase and lowercase).
            if char.isalpha():
                char = char.lower()
                # It includes at least one vowel.
                if not oneVowel and char in vowels:
                    oneVowel = True
                # It includes at least one consonant.
                elif not oneConsonant and char not in vowels:
                    oneConsonant = True
            elif not char.isnumeric():
                return False

        return oneVowel and oneConsonant


s = Solution()

print(s.isValid("234Ads"))  # 1
print(s.isValid("b3"))  # 0
print(s.isValid("a3$e"))  # 0
print(s.isValid("UuE6"))  # 0
