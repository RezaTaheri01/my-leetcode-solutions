class Solution: # not an efficient solution :)
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        betweenCols = abs(numRows - 2)
        currIndex = 0
        zigs = []
        while currIndex < len(s): # O(n)
            zigs.append(s[currIndex: currIndex + numRows].ljust(numRows))
            currIndex += numRows
            tmp = s[currIndex: currIndex + betweenCols].ljust(numRows)[::-1]
            tmp = tmp[1:] + ' '
            zigs.append(tmp)
            currIndex += betweenCols
            
        result = ''   
        for i in range(numRows): # O(n^2)
            for z in zigs:
                char = z[i]
                if char != ' ':
                    result += char        
            
        return result
    
s = Solution()
print(s.convert("PAYPALISHIRING", 3))
