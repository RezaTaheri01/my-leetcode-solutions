# Constraints:
#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

# Base Case: dp[0] = 0 (0 coins are needed for amount 0).
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # Initialize DP array with "infinity"
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:  # Process each coin
            for j in range(coin, amount + 1):  # Update DP array
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1




s = Solution()
print(s.coinChange([2, 5], 11))
print(s.coinChange([186,419,83,408], 6249))
