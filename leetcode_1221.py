class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rl_counter = 0
        result = 0

        for char in s:
            rl_counter += 1 if char == "R" else -1
            if rl_counter == 0:
                result += 1

        return result


s = Solution()

print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLRRRLLRLL"))
print(s.balancedStringSplit("LLLLRRRR"))
