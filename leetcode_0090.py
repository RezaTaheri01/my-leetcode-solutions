from typing import List


class Solution:        
    def subset_recur(self, i, subset):
        if i == self.length_nums:
            subset = sorted(list(subset))
            if subset not in self.subsets[len(subset)]:
                self.subsets[len(subset)] += [subset]
            return
        
        # include the current value
        subset.append(self.nums[i])
        self.subset_recur(i + 1, subset)
        
        # exclude the current value
        subset.pop()
        self.subset_recur(i + 1, subset)
               
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length_nums = len(nums)
        self.subsets = {key:[] for key in range(self.length_nums + 1)}
        
        self.subset_recur(0, [])
        
        result = []
        for sub_group in self.subsets.values():
            for sub in sub_group:
                result += [sub]

        return result                
    
    
s = Solution()
print(s.subsetsWithDup([0]))
print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([4,4,4,1,4]))
print(s.subsetsWithDup([4,1,0]))
