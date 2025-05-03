from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0

        c = 0
        for num in nums:
            if num == 0:
                result = max(result, c)
                c = -1
            c += 1

        return max(result, c)
    
    
s = Solution()

print(s.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(s.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))
