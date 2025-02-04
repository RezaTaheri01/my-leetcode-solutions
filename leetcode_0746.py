class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost)
        
        for i in range(2, n):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
            
        return min(cost[-1], cost[-2])




s = Solution()

# test cases
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6
print(s.minCostClimbingStairs([10,15,20])) # 15
