from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        self.result = []
        self.blocked_index = set() # stack

        def backtracking(current: List[int]):
            if len(current) == l:
                self.result.append(current)
                return

            visited = set()
            for i in range(l):
                if i not in self.blocked_index and nums[i] not in visited:
                    visited.add(nums[i])
                    self.blocked_index.add(i)
                    backtracking(current + [nums[i]])
                    self.blocked_index.remove(i)

        backtracking(current=[])

        return self.result


s = Solution()

print(s.permuteUnique([1]))
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))
