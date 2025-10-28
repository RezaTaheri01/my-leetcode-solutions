from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum12 = Counter(a+b for a in nums1 for b in nums2)
        counter = 0
        
        for num3 in nums3:
            for num4 in nums4:
                counter += sum12.get(-(num3 + num4), 0)
             
        return counter           
                        
                        
s = Solution()

print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(s.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))
