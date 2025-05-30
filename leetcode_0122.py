from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Iterate through the prices, buying at every dip and selling at the peak
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


s = Solution()
print(s.maxProfit([1, 5, 7])) # On each day, you may decide to buy and/or sell the stock.
