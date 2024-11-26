from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: list = []

        if not matrix:
            return result

        col, row = len(matrix) - 1, len(matrix[0]) - 1
        level = 0

        while level <= col and level <= row:
            # move right
            for i in range(level, row):
                result.append(matrix[level][i])

            # move down
            for j in range(level, col + 1):
                result.append(matrix[j][row])

            # move left
            if level < col:  # check if row left
                for i in range(row - 1, level - 1, -1):
                    result.append(matrix[col][i])

            # move up
            if level < row:  # check if column left
                for j in range(col - 1, level, -1):
                    result.append(matrix[j][level])

            level += 1
            col -= 1
            row -= 1

        return result

s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder([[6, 9, 7]]))
print(s.spiralOrder([[6], [9], [7]]))
print(s.spiralOrder([[6]]))
