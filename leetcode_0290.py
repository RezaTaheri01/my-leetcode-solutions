class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = pattern.upper()
        words = s.split()
        maps = {}
        
        if len(pattern) != len(words):
            return False

        for i, char in enumerate(pattern):
            if char not in maps:
                maps[char] = words[i]
            if words[i] not in maps:
                maps[words[i]] = char
            if maps[char] != words[i] or maps[words[i]] != char:
                return False

        return True


s = Solution()

print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "a a a a"))
print(s.wordPattern("abba", "a n n a"))
print(s.wordPattern("abba", "a n n a a"))
