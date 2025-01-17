class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []
        # determine minimum for each row and find max by list comprehension
        for row in matrix:
            minimum: int = min(row)

            index_minimum = row.index(minimum)
            # by using numpy, you can slice it
            maximum: int = max([r[index_minimum] for r in matrix])

            if minimum == maximum:
                result.append(minimum)

        return result


s = Solution()

print(s.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
print(s.luckyNumbers(matrix=[[1, 10, 4, 2], [
      9, 3, 8, 7], [15, 16, 17, 12]]))  # [12]
print(s.luckyNumbers(matrix=[[7, 8], [1, 2]]))  # [7]
