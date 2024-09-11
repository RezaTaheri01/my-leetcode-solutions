class Solution:
    def change_to_roman(self, digit, place_value, roman_map):
        number = int(digit) * place_value # 3749 => digit = 7 place_value = 100
        sym_first = '' # symbol that subtract sym
        if digit not in '49':
            sym = roman_map[place_value]
            count = number // place_value
            if count >= 5: # if true => we can use 5, 50, 500
                count -= 5
                sym_first = roman_map[place_value * 5]
            return sym_first + sym * count

        else:
            sym = roman_map[number + place_value]
            sym_first = roman_map[place_value]
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
        # 3 * 1000, 7 * 100, ...
        place_value = 1
        romans = ""
        
        for digit in str(num)[::-1]: # O(n) => n = len(num)
            
            # 2.convert each num in nums to roman base on 3 rules
            romans = (self.change_to_roman(digit, place_value, roman_map)) + romans
            place_value *= 10

        return romans


s = Solution()
print(s.intToRoman(58))
