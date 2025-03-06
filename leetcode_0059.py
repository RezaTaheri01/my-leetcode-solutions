from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        col, row = n - 1, n - 1
        level = 0
        current = 1

        while level <= col and level <= row:
            # move right
            for i in range(level, row):
                matrix[level][i] = current
                current += 1

            # move down
            for j in range(level, col + 1):
                matrix[j][row] = current
                current += 1

            # move left
            if level < col:  # check if row left
                for i in range(row - 1, level - 1, -1):
                    matrix[col][i] = current
                    current += 1

            # move up
            if level < row:  # check if column left
                for j in range(col - 1, level, -1):
                    matrix[j][level] = current
                    current += 1

            level += 1
            col -= 1
            row -= 1

        return matrix


s = Solution()

print(s.generateMatrix(n=1))
