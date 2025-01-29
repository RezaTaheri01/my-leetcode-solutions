class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return "0"

        stack = []
        # Turns out python can compare single string digits directly
        for digit in num:
            # Remove larger digits to minimize the number
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If k is still not zero, remove from the end
        stack = stack[:-k] if k else stack

        # Convert stack to number and remove leading zeros
        result = "".join(stack).lstrip("0")

        return result if result else "0"


s = Solution()

print(s.removeKdigits(num="143221999", k=3))
print(s.removeKdigits(num="1432200", k=4))
print(s.removeKdigits(num="10200", k=1))
print(s.removeKdigits(num="1123410", k=1))
print(s.removeKdigits(num="10", k=4))
print(s.removeKdigits(num="", k=2))
print(s.removeKdigits(num="1234567890", k=9))
