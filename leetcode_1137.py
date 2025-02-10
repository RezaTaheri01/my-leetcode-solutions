class Solution:
    def tribonacci(self, n: int) -> int:        
        if n < 3:
            return 0 if n == 0 else 1

        prev, nxt, current = 0, 1, 1 
        for _ in range(n - 2):
            prev, nxt, current = nxt, current, current + prev + nxt

        return current