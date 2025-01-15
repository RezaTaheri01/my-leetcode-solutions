# Todo: O(1) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls, lt = len(s) - 1, len(t) - 1
        if lt > ls:
            s, t = t, s
            ls, lt = lt, ls

        sRes, tRes = "", ""
        sBack, tBack = 0, 0

        while ls > -1:  # O(n)
            if s[ls] == '#':
                sBack += 1
            elif sBack > 0:
                sBack -= 1
            else:
                sRes += s[ls]
            ls -= 1

            if lt > -1:
                if t[lt] == '#':
                    tBack += 1
                elif tBack > 0:
                    tBack -= 1
                else:
                    tRes += t[lt]
                lt -= 1

        return sRes == tRes


s = Solution()
print(s.backspaceCompare(s="ab#c", t="ad#c"))  # True
print(s.backspaceCompare(s="ab##", t="c#d#"))  # True
print(s.backspaceCompare(s="ab#b", t="b"))  # False
print(s.backspaceCompare(s="bb######", t=""))  # True
