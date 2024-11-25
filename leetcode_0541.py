class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0
        while i < len(s):
            result += s[i: i+k][::-1]
            result += s[i+k: i+2*k]
            i += 2 * k

        return result


# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         # Convert string to list to allow in-place modifications
#         s = list(s)
#         n = len(s)

#         for i in range(0, n, 2 * k):
#             # Reverse the first k characters in every 2k block
#             s[i:i + k] = reversed(s[i:i + k])

#         # Join the list back into a string and return it
#         return ''.join(s)


s = Solution()
print(s.reverseStr('abcdefg', 2))
