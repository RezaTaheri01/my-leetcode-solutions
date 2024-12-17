# Todo: Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk
# where k >= 109, and you want to check one by one to see if t has its
# subsequence. In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Get the length of string `s`
        len_s = len(s)

        # If `s` is longer than `t`, it cannot be a subsequence
        if len_s > len(t):
            return False

        # Initialize a pointer to track the position in `s`
        index_s = 0

        # Iterate through each character in `t`
        for char in t:
            # If we've matched all characters in `s`, exit the loop early
            if index_s == len_s:
                break

            # If the current character in `t` matches the current character in `s`,
            # move to the next character in `s`
            if s[index_s] == char:
                index_s += 1

        # Check if we've matched all characters in `s`
        return index_s == len_s

# # Pythonic Solution
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         iter_t = iter(t)

#         return all(char in iter_t for char in s)


s = Solution()
# True, "abc" is a subsequence of "ahbgdc"
print(s.isSubsequence("abc", "ahbgdc"))
# False, "axc" is not a subsequence of "ahbgdc"
print(s.isSubsequence("axc", "ahbgdc"))
# True, an empty string is a subsequence of any string
print(s.isSubsequence("", "ahbgdc"))
# False, non-empty string cannot be a subsequence of an empty string
print(s.isSubsequence("abc", ""))
