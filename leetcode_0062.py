# Space O(m x n)
class Solution0:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D grid with zeros
        board = [[0] * n for _ in range(m)]
        
        # Fill the first row and first column with 1s
        for i in range(m):
            board[i][0] = 1
        for j in range(n):
            board[0][j] = 1
        
        # DP calculation
        for row in range(1, m):
            for col in range(1, n):
                board[row][col] = board[row - 1][col] + board[row][col - 1]
        
        return board[-1][-1]


# Space O(m + n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(m)]
        col = [1 for _ in range(n)] 
        
        for i in range(1, m):
            for j in range(1, n):
                tmp = row[i] + col[j]
                row[i] = tmp
                col[j] = tmp
    
        return row[-1]     
        

s = Solution()

print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(4, 2))
# print(s.uniquePaths(100, 100))
