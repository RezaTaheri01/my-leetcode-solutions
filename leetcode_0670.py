class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        length = len(digits)

        # max value, value index
        dp = [[0, 0] for _ in range(length)]
        dp[-1] = [num % 10, length - 1]

        # Precompute the max digit and its index to the right for each position
        for i in range(length - 2, -1, -1):
            current_digit = int(digits[i])
            dp[i] = max(dp[i+1], [current_digit, i])

        # Try to swap to get the max number
        for i in range(length):
            current_digit = int(digits[i])
            if current_digit < dp[i][0]:
                # Perform swap
                swap_index = dp[i][1]
                digits[i], digits[swap_index] = digits[swap_index], digits[i]
                return int("".join(digits))

        return num


s = Solution()

print(s.maximumSwap(2737))
print(s.maximumSwap(2736))
print(s.maximumSwap(9973))
print(s.maximumSwap(1993))
print(s.maximumSwap(12121212))
