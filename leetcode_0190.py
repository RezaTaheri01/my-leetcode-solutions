class Solution:
    def reverseBits(self, n: int) -> int:
        power = 0
        n = str(n)
        result = 0
        
        for d in n:
            if d == '1':
                result += 2 ** power
            power += 1

        print(result)


s = Solution()
s.reverseBits('00000010100101000001111010011100')
