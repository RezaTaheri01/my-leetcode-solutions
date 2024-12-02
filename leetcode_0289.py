class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        change_values = []

        def checkNeighbors(jc, ir):
            # Directions: Up, Down, Left, Right, Top-left, Top-right, Bottom-left, Bottom-right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]

            ones_counter = 0
            for dr, dc in directions:
                nr, nc = ir + dr, jc + dc
                # Check if the neighbor is within bounds
                if 0 <= nr < row and 0 <= nc < col:
                    if board[nc][nr] != 0:
                        ones_counter += 1

            # Rules
            if board[jc][ir] == 1:
                if ones_counter < 2:
                    change_values.append((jc, ir))
                elif ones_counter > 3:
                    change_values.append((jc, ir))
            else:
                if ones_counter == 3:
                    change_values.append((jc, ir))

        row, col = len(board[0]), len(board)
        # get what values need to be changed
        for j in range(col):
            for i in range(row):
                # check all neighbors
                checkNeighbors(j, i)
                
        for j, i in change_values:
            board[j][i] = 0 if board[j][i]==1 else 1
            
        print(board)


s = Solution()
s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
s.gameOfLife([[1, 1], [1, 0]])
s.gameOfLife([[1], [0]])
s.gameOfLife([[1]])




# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
