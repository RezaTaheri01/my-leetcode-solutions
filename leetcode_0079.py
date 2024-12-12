class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        r, c = len(board), len(board[0])
        lw = len(word)

        def traceback(j: int, i: int, wi: int) -> bool:
            # Base cases: out of bounds, character mismatch, or word found
            if not (0 <= j < r and 0 <= i < c) or board[j][i] != word[wi]:
                return False
            if wi == lw - 1:
                return True

            # Mark the cell as visited
            temp, board[j][i] = board[j][i], "#"

            # Explore all four directions
            for jd, id in directions:
                if traceback(j + jd, i + id, wi + 1):
                    return True

            # Restore the cell
            board[j][i] = temp
            return False

        # Iterate through the board to find the start position
        for sj in range(r):
            for si in range(c):
                if board[sj][si] == word[0] and traceback(sj, si, 0):
                    return True

        return False



s = Solution()  # T, F, F, T
print(s.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
print(s.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
print(s.exist([["a", "a"]], "aaa"))
print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
