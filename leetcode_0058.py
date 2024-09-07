class Solution:
    # O(n) Time
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        counter = 0 # O(1) Space
        
        for i in range(len(s) - 1, -1, -1): # O(1) Space
            if s[i] != " ":
                counter += 1
            elif counter > 0:
                break
            
        return counter
            
    
    
    
s = Solution()
print(s.lengthOfLastWord("Hello Reza"))