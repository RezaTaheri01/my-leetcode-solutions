from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        bits[-1] = -1
        i = 0
        
        while i < l - 1:
            if bits[i] == 1:
                if bits[i + 1] == -1:
                    return False
                i += 2
            else:
                i += 1 

        return True
    
    
    
s = Solution()

print(s.isOneBitCharacter([1,0,0])) # True
print(s.isOneBitCharacter([1,1,0])) # True
print(s.isOneBitCharacter([1, 0, 1, 1, 0, 0, 0, 1, 0])) # False
print(s.isOneBitCharacter([0])) # True
