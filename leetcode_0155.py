class MinStack:

    def __init__(self):
        self.minimum_stack: list = []
        self.stack: list = []
        self.repeat_c = 0

    def push(self, val: int) -> None:
        self.stack.append(val)  # O(1)

        if not self.minimum_stack or val <= self.minimum_stack[-1]:
            self.minimum_stack.append(val)  # O(1)

    def pop(self) -> None:
        if self.minimum_stack:
            val = self.stack.pop()  # O(1)
            if val == self.minimum_stack[-1]:
                self.minimum_stack.pop()  # O(1)

    def top(self) -> int:
        return self.stack[-1] if self.stack else None  # O(1)

    def getMin(self) -> int:
        return self.minimum_stack[-1] if self.minimum_stack else None  # O(1)


m = MinStack()
m.push(0)
m.push(1)
m.push(0)
print(m.getMin())
m.pop()
print(m.getMin())
