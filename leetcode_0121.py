from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # current_max = 0
        
        # # Iterate backwards through the list
        # for i in range(len(prices) - 1, -1, -1):
        #     current_max = max(current_max, prices[i])
        #     max_profit = max(max_profit, current_max - prices[i])
        
        # return max_profit

        min_buy = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit