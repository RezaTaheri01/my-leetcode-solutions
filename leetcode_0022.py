class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results: list[str] = []

        def backtracking(num: int, current: str, stack: int):
            if num == 0:
                results.append(current + ")" * stack)
                return

            # Add an open parenthesis
            backtracking(num - 1, current + "(", stack + 1)

            # Add a close parenthesis if valid
            if stack > 0:
                backtracking(num, current + ")", stack - 1)

        backtracking(n, "", 0)
        return results


s = Solution()
print(s.generateParenthesis(n=1))  # ["()"]
print(s.generateParenthesis(n=2))  # ["(())", "()()"]

# ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(n=3))

# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
print(s.generateParenthesis(n=4))

# print(s.generateParenthesis(n=10))
