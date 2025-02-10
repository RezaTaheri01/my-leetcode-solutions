import heapq

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        num1, num2 = heapq.nlargest(2, nums)
        
        return (num1 - 1) * (num2  -1)
