class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split(" ")
        words = s.split()
        # s = ""
        # for word in words[::-1]:
        #     if word != "":
        #         s += " " + word
                
        return " ".join(words[::-1]) # start from second index because of first space (line 7)
        
s = Solution()
print(s.reverseWords("  hello   world  "))