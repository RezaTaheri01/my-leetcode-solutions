from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start and end is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
             
        # Replace obstacles with -1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        
        # Fill the first row and first column with 1s until it reaches obstacle
        value = 1         
        for i in range(m):
            if obstacleGrid[i][0] == -1:
                value = 0
            else:
                obstacleGrid[i][0] = value    
        value = 1         
        for j in range(n):
            if obstacleGrid[0][j] == -1:
                value = 0
            else:
                obstacleGrid[0][j] = value
              
              
        # DP calculation
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == -1:
                    continue
                
                above = obstacleGrid[i - 1][j]
                left = obstacleGrid[i][j - 1]
                
                if above != -1:
                  obstacleGrid[i][j] += above  
                if left != -1:
                    obstacleGrid[i][j] += left
                    
        return obstacleGrid[-1][-1]
    
    

s = Solution()

print(s.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[1,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[0,0],[0,1]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[0]]))
         