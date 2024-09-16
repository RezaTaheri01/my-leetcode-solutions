class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_li = [']', ')', '}']
        chr_map = {']': '[', ')': '(', '}': '{'}

        for chr in s: # O(n)
            if chr in close_li: # O(3)
                # check last one in stack
                if not stack:
                    return False
                elif len(stack) > 0 and chr_map[chr] != stack.pop():
                    return False
            else:
                stack.append(chr)

        if not stack:
            return True
        return False


s = Solution()
print(s.isValid('(({({()})}))'))
