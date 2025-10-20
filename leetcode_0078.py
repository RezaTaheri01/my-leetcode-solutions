from typing import List


class Solution: 
    def subset_recursive(self, i, arr, res, subset):
        if i == len(arr):
            res.append(list(subset))
            return
        
        # include the current value and 
        self.subset_recursive(i + 1, arr, res, subset + [arr[i]])  
        
        # exclude the current value and 
        self.subset_recursive(i + 1, arr, res, subset)
          
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        
        # finding recursively
        self.subset_recursive(0, nums, result, subset)

        return result 
            
                
                       
s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([1]))
            
