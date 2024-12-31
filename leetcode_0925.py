class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_name, len_typed = len(name), len(typed)
        i, j = 0, 0
        while i < len_name:
            if j == len_typed or name[i] != typed[j]:
                return False
            if i + 1 < len_name and name[i] == name[i + 1]:
                j += 1
            else:
                while j < len_typed and name[i] == typed[j]:
                    j += 1
            i += 1

        return j == len_typed


s = Solution()

# Test cases
print(s.isLongPressedName("alex", "aaleexa"))  # False
print(s.isLongPressedName("leelee", "lleeelee"))  # True
print(s.isLongPressedName("alex", "aaleex"))  # True
print(s.isLongPressedName("saeed", "ssaaedd"))  # False
print(s.isLongPressedName("leelee", "lleeelee"))  # True
print(s.isLongPressedName("laiden", "laiden"))  # True
print(s.isLongPressedName("pyplrz", "ppyypllr"))  # False
print(s.isLongPressedName("a", "aaaa"))  # True
print(s.isLongPressedName("a", "b"))     # False
print(s.isLongPressedName("alex", "aaleexa"))  # False
print(s.isLongPressedName("rob", "robbby"))    # False
print(s.isLongPressedName("alex", "al"))   # False
print(s.isLongPressedName("lee", "l"))     # False
print(s.isLongPressedName("aabb", "aaaabbb"))  # True
print(s.isLongPressedName("aabb", "aabbb"))    # True
print(s.isLongPressedName("abc", "aabbcc"))  # True
print(s.isLongPressedName("abc", "aabcbc"))  # False
print(s.isLongPressedName("", ""))  # True
print(s.isLongPressedName("", "a"))  # False
print(s.isLongPressedName("alex", ""))  # False
print(s.isLongPressedName("aaabb", "aaaabbbbbb"))  # True
print(s.isLongPressedName("aaabb", "aaaabbbbbbc"))  # False
print(s.isLongPressedName("aab", "aaabbc"))        # False
print(s.isLongPressedName("a" * 1000, "a" * 2000))  # True
print(s.isLongPressedName("a" * 1000 + "b", "a" * 2000))  # False
