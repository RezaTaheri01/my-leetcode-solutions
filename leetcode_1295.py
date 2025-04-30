from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
       return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))
   
   
        
s = Solution()

print(s.findNumbers(nums = [12,345,2,6,7896]))
