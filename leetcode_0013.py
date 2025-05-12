class Solution:
    def __init__(self):
        self.mapper: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and self.mapper[s[i]] < self.mapper[s[i + 1]]:
                result += self.mapper[s[i + 1]] - self.mapper[s[i]]
                i += 2
            else:
                result += self.mapper[s[i]]
                i += 1

        return result


            
    
    
s = Solution()

print(s.romanToInt("VIII"))
