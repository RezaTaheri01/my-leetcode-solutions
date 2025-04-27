# Constraints:
#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

# Base Case: dp[0] = 0 (0 coins are needed for amount 0).
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if coin > a:
                    break
                dp[a] = min(dp[a], 1 + dp[a - coin])
    
        return dp[amount] if dp[amount] != amount + 1 else -1
    




s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([186,419,83,408], 6249))
