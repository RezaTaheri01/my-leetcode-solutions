from typing import List


class Solution:
    def eachBox(self, mat, i, j):
        nums = []
        for r in range(i, i + 3):  # row
            for c in range(j, j + 3):  # column
                tmp = mat[r][c]
                if tmp != ".":
                    if tmp in nums:
                        return False
                    nums.append(tmp)
        return True

    def eachLine(self, mat, i, j, length):
        nums = []
        if i == 0:  # horizontal
            for it in range(length):
                tmp = mat[j][it]
                if tmp != ".":
                    if tmp in nums:
                        return False
                    nums.append(tmp)

        nums = []
        if j == 0:  # vertical
            for jt in range(length):
                tmp = mat[jt][i]
                if tmp != ".":
                    if tmp in nums:
                        return False
                    nums.append(tmp)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)

        # first check 3x3 boxes
        for j in range(0, length, 3):
            for i in range(0, length, 3):
                if not self.eachBox(board, i, j):
                    return False

        # second check lines vertical and horizontal
        for ij in range(length):
            if not self.eachLine(board, 0, ij, length):
                return False
            if not self.eachLine(board, ij, 0, length):
                return False

        return True


s = Solution()
print(s.isValidSudoku([[".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["8", ".", ".", ".", ".", "7", ".", ".", "."],
                       [".", ".", ".", "8", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", "9", ".", "2", ".", "5"],
                       ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", "3", ".", ".", "6", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", "8", "."],
                       [".", ".", "9", ".", ".", ".", ".", ".", "."]]))
