class Solution:
    def generateTag(self, caption: str) -> str:
        tag = ""
        
        for word in caption.split():
            tag += word.capitalize() if tag else word.lower() 
            
        return "#" + tag[:99]
    
    
s = Solution()

print(s.generateTag(caption = "LeetCode daily streak achieved"))
print(s.generateTag(caption = "can I Go There"))
print(s.generateTag(caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"))
print(s.generateTag(caption = "m"))
print(s.generateTag(caption = "   "))
