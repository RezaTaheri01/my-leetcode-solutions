from collections import Counter
from typing import List
import math

# GCD of two or more numbers is the largest number
# that divides all of the respective numbers without leaving a remainder.

# LCM of two or more numbers is the smallest multiple 
# that is divisible by all the respective numbers.
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck).values()
        return math.gcd(*counter) > 1
    
    
s = Solution()
print(s.hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(s.hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))
print(s.hasGroupsSizeX(deck = [2, 2]))
print(s.hasGroupsSizeX(deck = [2, 1]))
print(s.hasGroupsSizeX(deck = [1]))
print(s.hasGroupsSizeX(deck = []))

print(s.hasGroupsSizeX(deck = [1,1,1,1,2,2,2,2,2,2])) # True
print(s.hasGroupsSizeX(deck = [0,0,0,1,1,1,1,1,1,2,2,2,3,3,3])) # True
