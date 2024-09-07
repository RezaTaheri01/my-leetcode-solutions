class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convert_dec(num):
            dec = 0
            power = 0
            for d in num[::-1]:
                if d == "1":
                    dec += 2 ** power
                power += 1

            return dec

        def convert_to_bin(result):
            bin_str = ''
            while result > 0:
                bin_str += str(result % 2)
                result = result // 2
                
            return bin_str[::-1]

        a = convert_dec(a)
        b = convert_dec(b)

        return convert_to_bin(a + b)


s = Solution()
print(s.addBinary("1010", "1011"))