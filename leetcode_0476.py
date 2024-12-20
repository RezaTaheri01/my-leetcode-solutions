class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        
        rev_binary = ""
        for b in binary:
            rev_binary += "0" if b == "1" else "1"
            
        return int(rev_binary, 2)


s = Solution()
print(s.findComplement(5))