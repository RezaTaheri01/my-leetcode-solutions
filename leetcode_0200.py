# Todo: BFS with queue

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def near_lands(it: int, jt: int):
            if grid[it][jt] == "0" or it * m + jt in visited:
                return
            visited.add(it * m + jt)
            if jt > 0:  # left
                near_lands(it, jt - 1)
            if jt < m - 1:  # right
                near_lands(it, jt + 1)
            if it > 0:  # up
                near_lands(it - 1, jt)
            if it < n - 1:  # down
                near_lands(it + 1, jt)

        n, m = len(grid), len(grid[0])
        visited: set = set()
        counter = 0

        for i in range(n):
            for j in range(m):
                # i * m + j => flattens 2D indices into 1D
                if grid[i][j] == "1" and i * m + j not in visited:
                    counter += 1
                    near_lands(i, j)

        return counter


s = Solution()

print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

print(s.numIslands(grid=[["1", "1", "1"],
                         ["0", "1", "0"],
                         ["1", "1", "1"]]))
