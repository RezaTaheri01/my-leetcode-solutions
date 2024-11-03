# You must write an algorithm that runs in O(n) time. Done!
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)  # Convert list to set for O(1) lookups
        max_streak = 0  # Initialize the max streak

        for num in nums_set:
            # Check if `num` is the start of a sequence
            if num - 1 not in nums_set:
                streak = 1
                current_num = num + 1

                # Count consecutive numbers
                while current_num in nums_set:
                    streak += 1
                    current_num += 1

                # Update max_streak if this sequence is the longest so far
                max_streak = max(max_streak, streak)

        return max_streak



# [2, 4, 1, 3, 5]
s = Solution()
print(s.longestConsecutive([2, 4, 1, 3, 5]))
