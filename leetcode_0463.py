from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row: int = len(grid)
        col: int = len(grid[0])
        directions: List[tuple[int, int]] = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def check_four_side(i: int, j: int) -> int:
            count: int = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= row or nj < 0 or nj >= col or grid[ni][nj] == 0:
                    count += 1
            return count

        perimeter: int = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += check_four_side(r, c)

        return perimeter


# from leetcode sample codes
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         perimeter = 0

#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 1:  # If the cell is land
#                     # Add 4 for the cell itself
#                     perimeter += 4

#                     # Subtract 2 for each adjacent land cell
#                     if i > 0 and grid[i-1][j] == 1:  # Check top
#                         perimeter -= 2
#                     if j > 0 and grid[i][j-1] == 1:  # Check left
#                         perimeter -= 2
