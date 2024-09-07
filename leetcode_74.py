class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # edge case
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        # find which row to search
        low, high = 0, rows
        while low <= high:
            mid = (low + high) // 2
            guess = matrix[mid][cols]
            if matrix[mid][0] <= target <= matrix[mid][cols]:
                break
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return False
        # search for target
        nums = matrix[mid]
        low, high = 0, cols
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return True
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


s = Solution()
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20]], target=3))
