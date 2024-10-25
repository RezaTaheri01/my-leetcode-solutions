class Solution:  # O(h * n)
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        # edge case
        if needle_len > haystack_len:
            return -1

        # Check each starting index in haystack
        for i in range(haystack_len - needle_len + 1):
            if haystack[i] == needle[0] and haystack[i + needle_len - 1] == needle[-1]:
                for j in range(1, needle_len):
                    if haystack[i + j] != needle[j]:
                        break
                else:  # If the inner loop completes without break the else clause is executed
                    return i
        return -1


s = Solution()
print(s.strStr("sadbutdad", "dad"))
