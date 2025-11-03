from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0

        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                if neededTime[i] <= neededTime[i + 1]:
                    total_time += neededTime[i]
                else:
                    total_time += neededTime[i + 1]
                    neededTime[i+1] = neededTime[i]

        return total_time
