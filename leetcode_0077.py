class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:        
        def backtracking(start: int = 1, path: list = []):
            if len(path) == k:
                result.append(path[:])
                return
            
            # Only iterate to a point where there are enough numbers left
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()
            
        result = []
        backtracking()
        return result

s = Solution()
print(s.combine(4, 2))
