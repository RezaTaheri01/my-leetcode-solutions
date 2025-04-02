class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        max_i = nums[0]
        max_diff = float("-inf")
        max_triplet = 0

        for j in range(1, len(nums) - 1):
            max_diff = max(max_diff, max_i - nums[j])

            max_triplet = max(max_triplet, max_diff * nums[j + 1])

            max_i = max(max_i, nums[j])

        return max_triplet


s = Solution()

print(s.maximumTripletValue(nums=[1, 10, 3, 4, 19]))
print(s.maximumTripletValue(nums=[12, 6, 1, 2, 7]))
print(s.maximumTripletValue(nums=[-12, -6, 1]))
print(s.maximumTripletValue(nums=[1, 2, 3]))
print(s.maximumTripletValue(nums = [10, 1, 100, 2, 1000]))
print(s.maximumTripletValue(nums = [100, 50, 1, 10, 1000]))
