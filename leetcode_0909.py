from collections import deque

class Solution:
    def matrix_to_list(self, board: list[list[int]]) -> list[int]:
        n = len(board)
        flat_board = [-1] * (n * n)  # Initialize a flat list to represent the board

        # Convert the matrix into a 1D list with boustrophedon labeling
        for i in range(n):
            if i % 2 == 0:  # Even rows (start from left to right)
                for j in range(n):
                    flat_board[i * n + j] = board[n - 1 - i][j]
            else:  # Odd rows (start from right to left)
                for j in range(n):
                    flat_board[i * n + (n - 1 - j)] = board[n - 1 - i][j]

        return flat_board

    def bfsSearch(self, board: list[int], n: int) -> int:
        visited = [False] * (n * n)
        queue = deque([0])  # Start from position 0 (square 1)
        visited[0] = True
        moves = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                # If we reached the last square (n^2 - 1)
                if current == n * n - 1:
                    return moves

                # Explore the next 6 possible positions
                for step in range(1, 7):
                    next_pos = current + step
                    if next_pos < n * n and not visited[next_pos]:
                        visited[next_pos] = True

                        # If there's a ladder or snake, move to its destination
                        if board[next_pos] != -1:
                            next_pos = board[next_pos] - 1  # Move to the destination of the snake/ladder

                        queue.append(next_pos)

            moves += 1  # Increment the move count after each level

        return -1  # If we can't reach the last square

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        flat_board = self.matrix_to_list(board)  # Flatten the board according to boustrophedon

        return self.bfsSearch(flat_board, n)