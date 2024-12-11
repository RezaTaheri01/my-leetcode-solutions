class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combos: list[list[int]] = []
        l: int = len(candidates)

        def backtracking(start: int, combo: list[int], remaining_sum: int):
            if remaining_sum == 0:
                combos.append(combo[:])
                return
            if remaining_sum < 0:
                return

            for i in range(start, l):
                candidate = candidates[i]
                combo.append(candidate)
                # Allow reuse of the same element
                backtracking(i, combo, remaining_sum - candidate)
                combo.pop()

        backtracking(0, [], target)
        return combos


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
