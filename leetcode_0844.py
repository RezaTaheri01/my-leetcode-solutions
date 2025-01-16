class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        sBack, tBack = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    sBack += 1
                    i -= 1
                elif sBack > 0:
                    sBack -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == "#":
                    tBack += 1
                    j -= 1
                elif tBack > 0:
                    tBack -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True


s = Solution()
print(s.backspaceCompare(s="ab#c", t="ad#c"))  # True
print(s.backspaceCompare(s="ab##", t="c#d#"))  # True
print(s.backspaceCompare(s="ab#b", t="b"))  # False
print(s.backspaceCompare(s="bb###", t=""))  # True
