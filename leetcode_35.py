class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid

            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
                

        return low
    
s = Solution()
print(s.searchInsert([1,3,5,6], 2))