from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        sum_nums = n * (n + 1) // 2
        seen: set = set()
        
        for row in grid:
            for num in row:
                if num not in seen:
                    seen.add(num)
                    sum_nums -= num
                else:
                    duplicate = num
        
        return [duplicate, sum_nums]


s = Solution()

print(s.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]))
print(s.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
