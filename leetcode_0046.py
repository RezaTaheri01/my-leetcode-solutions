class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        combos: list[list[int]] = []

        def backtracking(numbers: list[int], combo: list[int] = []):
            if not numbers:
                combos.append(combo[:])
                return
            
            for i in range(len(numbers)):
                # Choose
                num = numbers.pop(i)
                combo.append(num)
                # Explore
                backtracking(numbers, combo)
                # Un choose
                combo.pop()
                numbers.insert(i, num)

        backtracking(nums)
        return combos


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s = Solution()
print(s.permute(nums=[1, 2, 3]))


# from itertools import permutations

# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         return list(map(list, permutations(nums)))