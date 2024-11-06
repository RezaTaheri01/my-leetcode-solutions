class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  # target = 0
        results = []
        n = len(nums)

        # Sort the elements
        nums.sort()

        # Fix the first element one by one
        # and find the other two elements
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate for the fixed element
                continue

            l, r = i + 1, n - 1  # Set left and right pointers

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    results.append([nums[i], nums[l], nums[r]])

                    # # Skip duplicates for the second and third elements
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move pointers after processing duplicates
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:  # curr_sum > 0
                    r -= 1

        return results


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSum([-2, 0, 1, 1, 2]))
