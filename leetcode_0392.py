from bisect import bisect_right  # binary search tree

# Todo: Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk
# where k >= 109, and you want to check one by one to see if t has its
# subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequenceList(self, s_list: list[str], t: str) -> bool:
        # Preprocess t: create a map of character positions
        char_positions = {}
        for i, char in enumerate(t):
            if char not in char_positions:
                char_positions[char] = []
            char_positions[char].append(i)

        results = []
        for s in s_list:
            if not s:
                results.append(True)
                continue

            prev_pos = -1
            is_valid = True
            for char in s:
                if char not in char_positions:
                    is_valid = False
                    break

                positions = char_positions[char]
                idx = bisect_right(positions, prev_pos)
                if idx >= len(positions):
                    is_valid = False
                    break
                prev_pos = positions[idx]

            results.append(is_valid)

        return results

    def isSubsequence(self, s: str, t: str) -> bool:
        # Get the length of string `s` and `t`
        n, m = len(s), len(t)

        # If `s` is longer than `t`, it cannot be a subsequence
        if n > m:
            return False
        if n == m:
            return s == t

        # Initialize a pointer to track the position in `s`
        index_s = 0
        # Iterate through each character in `t`
        for char in t:
            # If we've matched all characters in `s`, exit the loop early
            if index_s == n:
                break

            # If the current character in `t` matches the current character in `s`,
            # move to the next character in `s`
            if s[index_s] == char:
                index_s += 1

        # Check if we've matched all characters in `s`
        return index_s == n

    def isSubsequencePythonic(self, s: str, t: str) -> bool:
        iter_t = iter(t)
        return all(char in iter_t for char in s)


s = Solution()

# True, "abc" is a subsequence of "ahbgdc"
print(s.isSubsequence("abc", "ahbgdc"))
# False, "axc" is not a subsequence of "ahbgdc"
print(s.isSubsequence("axc", "ahbgdc"))
# True, an empty string is a subsequence of any string
print(s.isSubsequence("", "ahbgdc"))
# False, non-empty string cannot be a subsequence of an empty string
print(s.isSubsequence("abc", ""))

# True, True, False, False
print(s.isSubsequenceList(["abc", "aac", "aaab", "aaaa"], "ahabgdadc"))
