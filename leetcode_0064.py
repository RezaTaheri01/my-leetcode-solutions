from typing import List
# import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)): # O(m)
            grid[i][0] += grid[i - 1][0]
            
        for j in range(1, len(grid[0])): # O(n)
            grid[0][j] += grid[0][j - 1]
        
        # O(m x n)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        return grid[-1][-1]
        
        
s = Solution()

print(s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))

# np.random.seed(42)      
# grid = np.random.randint(0, 200, size=(200, 200))
# print(s.minPathSum(grid = list(grid)))
