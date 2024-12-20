class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x: str = bin(x)[2:]
        bin_y: str = bin(y)[2:]

        lx, ly = len(bin_x), len(bin_y)
        if lx > ly:
            bin_x, bin_y = bin_y, bin_x
        bin_x = "0" * abs(lx - ly) + bin_x
            
        counter: int = 0 
        for index in range(len(bin_x)):
            if bin_x[index] != bin_y[index]:
                counter += 1
                
        return counter


# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         result: str = x ^ y # Xor
        
#         return bin(result).count("1")


s = Solution()
print(s.hammingDistance(4, 2))
