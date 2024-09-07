class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        
        for char in s:
            if char == '(':
                stack.append([])
            elif char == ')':
                last = stack.pop()
                stack[-1].extend(reversed(last)) # extend
            else:
                stack[-1].append(char)
        return "".join(stack[-1])
    
    
s = Solution()
print(s.reverseParentheses("(u(love)i)"))