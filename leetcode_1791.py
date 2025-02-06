# 3 <= n <= 105
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return sum(set(edges[0]) & set(edges[1]))
    
    
s = Solution()
print(s.findCenter([[1,2],[5,1],[1,3],[1,4]]))
