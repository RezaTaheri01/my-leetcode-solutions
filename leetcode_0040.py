from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtracking(start: int, current: List[int], total: int):
            if total == target:
                result.append(current)
                return
            if total > target:
                return 

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if total + candidates[i] > target:
                    break   # safe pruning here
                
                backtracking(i + 1, current + [candidates[i]], total + candidates[i])


        backtracking(0, [], 0)

        return result


s = Solution()

print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(s.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
print(s.combinationSum2(candidates = [1, 2, 3, 5], target = 6))
