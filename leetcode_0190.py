class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]  # dec to bin
        n = (32 - len(str(n))) * "0" + str(n)  # make sure that len(n) == 32

        power = 0
        result = 0

        # convert bin to dec
        for d in n:  # reverse iteration
            if d == '1':
                result += 2 ** power
            power += 1

        return result


s = Solution()
print(s.reverseBits(43261596))
