class Solution:
    def jump(self, nums: list[int]) -> int:
        end = len(nums) - 1
        max_reach = 0
        steps = 0
        current_jump_end = 0

        for i in range(end):
            # Update the furthest point reachable from current position
            max_reach = max(max_reach, i + nums[i])
            
            # If we've reached the end of the current jump
            if i == current_jump_end:
                steps += 1
                current_jump_end = max_reach

                # Early exit if we can reach the last index
                if current_jump_end >= end:
                    break

        return steps

# Example usage:
s = Solution()
print(s.jump([2, 1, 1, 1, 1]))  # Output should be 3
