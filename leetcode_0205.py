class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = self.check(s, t)
        b = self.check(t, s)
        if not a or not b:
            return False
        return True

    def check(self, s, t):
        hashMap = {}
        tC = sC = ''
        for i in range(len(s)):
            tC, sC = t[i], s[i]
            if tC not in hashMap:
                hashMap[tC] = sC
            elif hashMap[tC] != sC:
                return False
        return True
                    
s = Solution()
print(s.isIsomorphic("egg", "foo"))