from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        result = -1
        for val, count in Counter(arr).items():
            if val == count and val > result:
                result = val
        return result
    
    
    
s = Solution()

print(s.findLucky(arr = [2,2,3,4]))
print(s.findLucky(arr = [2,2,2,3,3]))
print(s.findLucky(arr = [1,2,2,3,3,3]))