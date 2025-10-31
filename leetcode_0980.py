from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        non_obstacle_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_point = (i, j)
                elif grid[i][j] != -1:
                    non_obstacle_count += 1

        def dfs(i, j, count):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == -1:
                return 0

            if grid[i][j] == 2:
                return 1 if count == non_obstacle_count else 0

            tmp = grid[i][j]
            grid[i][j] = -1

            paths = (dfs(i + 1, j, count + 1) +
                     dfs(i - 1, j, count + 1) +
                     dfs(i, j + 1, count + 1) +
                     dfs(i, j - 1, count + 1))

            grid[i][j] = tmp

            return paths

        return dfs(start_point[0], start_point[1], 0)


s = Solution()
print(s.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(s.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print(s.uniquePathsIII(grid=[[0, 1], [2, 0]]))
