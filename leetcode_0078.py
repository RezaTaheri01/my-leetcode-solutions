# https://www.geeksforgeeks.org/dsa/backtracking-to-find-all-subsets/
# https://media.geeksforgeeks.org/wp-content/uploads/20230911132238/print-all-subsets.png
from typing import List

class Solution:  
    def subset_recur(self, i, subset):
        if i == self.length_nums:
            self.result.append(list(subset))
            return
        
        # include the current value
        subset.append(self.nums[i])
        self.subset_recur(i + 1, subset)
        
        # exclude the current value
        subset.pop()
        self.subset_recur(i + 1, subset)
               
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length_nums = len(nums)
        self.result = []
        
        self.subset_recur(0, [])
        
        return self.result
            
                
                       
s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([1]))
            
