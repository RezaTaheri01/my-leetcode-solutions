class Solution:
    def clearDigits(self, s: str) -> str:
        # The input is generated such that it is possible to delete all digits.
        stack = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            elif stack:
                stack.pop()
                
        return "".join(stack)
                

s = Solution()
print(s.clearDigits("cb34b"))
print(s.clearDigits("abc"))
