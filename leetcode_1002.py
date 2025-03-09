from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        
        for word in words[1:]:
            common &= Counter(word)
            
        return list(common.elements())
            
            
   
s = Solution()
        
print(s.commonChars(words = ["bella","label","roller"])) # ["e","l","l"]
print(s.commonChars(words = ["cool","lock","cook"])) # ["c","o"]
