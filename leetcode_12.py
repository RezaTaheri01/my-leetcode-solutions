class Solution:
    def change_to_roman(self, digit, power, roman_map):
        number = int(digit) * power
        sym_first = ''
        if digit not in '49':
            sym = roman_map[power]
            count = number // power
            if count >= 5:
                count -= 5
                sym_first = roman_map[power * 5]
            return sym_first + sym * count

        else:  # Ok
            sym = roman_map[number + power]
            sym_first = roman_map[power]
            return sym_first + sym

    def intToRoman(self, num: int) -> str:
        roman_map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        if num == 0:
            return ''
        # 1.Divide digits like 3749 -> 3000, 700, 40, 9
        power = 1
        romans = []
        for digit in str(num)[::-1]:
            # 2.convert each num in nums to roman base on 3 rules
            romans.append(self.change_to_roman(digit, power, roman_map))
            power *= 10

        return "".join(romans[::-1])


s = Solution()
print(s.intToRoman(58))
