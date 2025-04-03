from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i, j = 0, 0
        content = 0
        
        while i < n and j < m:
            if g[i] <= s[j]:
                content += 1
                i += 1
            j += 1

        return content


s = Solution()

print(s.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(s.findContentChildren(g=[1, 2, 3], s=[1, 2, 3]))
print(s.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8])) # [7, 8, 9 , 10], [5, 6, 7, 8]
