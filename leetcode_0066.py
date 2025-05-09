from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        preserve = 1
        for i in range(len(digits) - 1, -1, -1):
            if preserve == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += preserve
                    preserve = 0
            else:
                break
            
        if preserve == 1:
            digits.insert(0, 1)

        return digits
    
    
    
s = Solution()

print(s.plusOne([9]))
print(s.plusOne([9, 9]))
print(s.plusOne([1, 1]))
