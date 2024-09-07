class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        betweenRows = abs(numRows - 2)
        currIndex = 0
        zigs = []
        while currIndex < len(s):
            zigs.append(s[currIndex: currIndex + numRows].ljust(numRows))
            currIndex += numRows
            tmp = s[currIndex: currIndex + betweenRows].ljust(numRows)[::-1]
            tmp = tmp[1:] + ' '
            zigs.append(tmp)
            currIndex += betweenRows
            
        # print(zigs)
        result = ''   
        for i in range(numRows):
            for z in zigs:
                char = z[i]
                if char != ' ':
                    result += char        
            
        return result
    
s = Solution()
print(s.convert("AB", 1))