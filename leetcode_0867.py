from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        transposed = [[None] * r for row in range(c)]

        for i in range(r):
            for j in range(c):
                transposed[j][i] = matrix[i][j]


        return transposed