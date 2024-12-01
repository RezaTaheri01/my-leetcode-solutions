class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix) - 1  # n x n
        for j in range((n + 1) // 2):
            # find corners: right, left, left down, right down
            c: list = [(j, n - j), (n - j, n - j), (n - j, j), (j, j)]
            # print(c) # check corners
            for i in range(j, n - j):
                # there is an other implementation for this section at end of this file
                move = i - j
                tmp = matrix[j][i]
                for m in range(4):  # 4 Side
                    cj, ci = c[m][0], c[m][1]
                    chng = 1 if (m == 0 or m == 3) else -1

                    if m == 0 or m == 2:
                        tmp, matrix[cj + (move * chng)][ci] = matrix[cj + (move * chng)][ci], tmp
                    else:
                        tmp, matrix[cj][ci + (move * chng)] = matrix[cj][ci + (move * chng)], tmp

        print(matrix) # result of rotation


s = Solution()

s.rotate([[5]])
s.rotate([[1, 2], [3, 4]])
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
s.rotate([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# correct results in order
# [[5]]
# -------------------------------------------------
# [[3, 1], [4, 2]]
# -------------------------------------------------
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# -------------------------------------------------
# [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
# -------------------------------------------------
# [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]


# The other implementation:
# for i in range(j, n - j):
#     move =  i - j
#     # right col down
#     tmp, matrix[c[0][0] + move][c[0][1]] = matrix[c[0][0] + move][c[0][1]], matrix[j][i]
#     # bottom row
#     tmp, matrix[c[1][0]][c[1][1] - move] = matrix[c[1][0]][c[1][1] - move] , tmp
#     # left col
#     tmp, matrix[c[2][0] - move][c[2][1]] = matrix[c[2][0] - move][c[2][1]] , tmp
#     # top row
#     tmp, matrix[c[3][0]][c[3][1] + move] = matrix[c[3][0]][c[3][1] + move] , tmp
