class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_sum = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                profit_sum += prices[i+1] - prices[i]

        return profit_sum
