class Solution:
    def __init__(self):
        self.fib_sequence: list = [0, 1]  # Base cases

    def fib(self, n: int) -> int:
        if len(self.fib_sequence) > n:
            return self.fib_sequence[n]

        prev, current = self.fib_sequence[-2], self.fib_sequence[-1]
        for _ in range(n - len(self.fib_sequence) + 1):
            prev, current = current, prev + current
            self.fib_sequence.append(current)

        return self.fib_sequence[n]
        