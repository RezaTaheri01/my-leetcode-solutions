class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calGain(s, first: str, second: str, score_first: int, score_second: int):
            score = 0
            stack, stack2 = []
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += score_first
                else:
                    stack.append(char)
            for char in stack:
                if stack2 and stack2[-1] == second and char == first:
                    stack.pop()
                    score += score_second
                else:
                    stack2.append(char)

            return score

        return calGain(s, 'a', 'b', x, y) if x > y else calGain(s, 'b', 'a', y, x)
