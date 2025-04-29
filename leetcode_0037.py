from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            box_id = (i // 3) * 3 + j // 3
            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_id].add(num)

                    if backtrack(index + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0)


s = Solution()

s.solveSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

s.solveSudoku([[".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", "9", ".", ".", "1", ".", ".", "3", "."],
               [".", ".", "6", ".", "2", ".", "7", ".", "."],
               [".", ".", ".", "3", ".", "4", ".", ".", "."],
               ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", "2", "5", ".", "6", "4", ".", "."],
               [".", "8", ".", ".", ".", ".", ".", "1", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."]])
