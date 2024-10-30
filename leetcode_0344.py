class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start_p = 0
        end_p = len(s) - 1

        while start_p < end_p:
            s[start_p], s[end_p] = s[end_p], s[start_p]
            start_p += 1
            end_p -= 1

