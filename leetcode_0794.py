from collections import Counter


class Solution:
    def __init__(self):
        self.diagonals = (((0, 0), (1, 1), (2, 2)),
                          ((0, 2), (1, 1), (2, 0)))

    def countWins(self, board):
        def _countWins(pos):
            prev = None
            for i, j in pos:
                if (prev and prev != board[i][j]) or board[i][j] == ' ':
                    return 0
                prev = board[i][j]
            else:
                chars.append(prev)
                return 1

        counter = 0
        chars = []

        for pos in self.diagonals:
            counter += _countWins(pos)

        for i in range(3):
            counter += _countWins([(i, j) for j in range(3)])
            counter += _countWins([(j, i) for j in range(3)])

        return counter, chars

    def validTicTacToe(self, board: list[str]) -> bool:
        # X should be +1 or equal to O characters
        counter = Counter(''.join(board))
        diff = counter.get('X', 0) - counter.get('O', 0)
        if diff < 0 or diff > 1:
            return False

        # Count wins
        w_counter, w_chars = self.countWins(board)
        if w_counter > 2 or (w_counter == 2 and 'O' in w_chars):
            return False

        # If both of wins are X, There is only one valid solution
        if w_counter == 2 and (sum(counter.values()) != 9 or counter.get('O', 0) != 4):
            return False

        # Final move should be X
        if w_counter == 1 and 'X' in w_chars and diff == 0:
            return False

        # Final move should be O
        if w_counter == 1 and 'O' in w_chars and diff == 1:
            return False

        return True


s = Solution()

print(s.validTicTacToe(board=["O  ", "   ", "   "]))  # False
print(s.validTicTacToe(board=["   ", "   ", "   "]))  # True
print(s.validTicTacToe(board=["XOO", "   ", "   "]))  # False
print(s.validTicTacToe(board=["XOX", " X ", "   "]))  # False
print(s.validTicTacToe(board=["XOX", "O O", "XOX"]))  # True
print(s.validTicTacToe(board=["XXX", "OOX", "OOX"]))  # True
print(s.validTicTacToe(board=["OXX", "OOX", "OOX"]))  # False
print(s.validTicTacToe(board=["XXX", "XOO", "OO "]))  # False
print(s.validTicTacToe(board=["OXX", "XOX", "OXO"]))  # False
