from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        not_guarded = m * n
        not_guarded -= (len(walls) + len(guards))
        board = [[0] * n for _ in range(m)]

        for i, j in walls:
            board[i][j] = 1  # wall

        for i, j in guards:
            board[i][j] = 2  # guard

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i, j in guards:
            for dx, dy in directions:
                x, y = i + dx, j + dy
                while 0 <= x < m and 0 <= y < n and board[x][y] != 1 and board[x][y] != 2:
                    if board[x][y] == 0:  # unguarded so far
                        board[x][y] = 3   # now guarded
                        not_guarded -= 1
                        
                    x += dx
                    y += dy

        return not_guarded


s = Solution()
print(s.countUnguarded(m=4, n=6, guards=[
      [0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))

print(s.countUnguarded(m=3, n=3, guards=[
      [1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]))

print(s.countUnguarded(m=1000, n=100, guards=[
      [1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]))

print(s.countUnguarded(m=1, n=1, guards=[], walls=[[0, 0]]))

print(s.countUnguarded(m=2, n=7, guards=[[1,5],[1,1],[1,6],[0,2]], walls=[[0,6],[0,3],[0,5]]))

