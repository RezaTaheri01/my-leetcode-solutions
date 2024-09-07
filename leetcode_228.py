class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        nums.append(float('inf'))
        prev = nums.pop(0)
        start = prev
        res = []
        for num in nums:
            if num != prev + 1:
                if prev == start:
                    res.append(f'{prev}') 
                else:
                    res.append(f'{start}->{prev}')
                start = num
            prev = num
        return res
    
s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))