# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0.find zeros
        zeros: list = []  # zeros positions
        row, col = len(matrix[0]), len(matrix)

        for i in range(row):  # O(n x m)
            for j in range(col):
                zeros.append((j, i)) if matrix[j][i] == 0 else None

        # 1.zero rows and cols
        for jz, iz in zeros:
            for i in range(row):
                matrix[jz][i] = 0
            for j in range(col):
                matrix[j][iz] = 0

        # print(matrix)


s = Solution()
s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
s.setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
