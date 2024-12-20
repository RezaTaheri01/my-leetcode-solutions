# Todo: Improve it
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i, price in enumerate(prices):
            for discount in prices[i+1:]:
                if price >= discount:
                    prices[i] -= discount
                    break
                    
        return prices
    
    
    
s = Solution()
print(s.finalPrices([8,4,6,2,3]))
        