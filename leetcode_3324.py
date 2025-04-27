from typing import List


class Solution:
    def __init__(self):
        self.alphabet = [chr(i) for i in range(97, 123)]

    def stringSequence(self, target: str) -> List[str]:
        result: list[str] = []
        prefix: str = ""

        for char in target:
            current_index = 0
            while char != self.alphabet[current_index]:
                result.append(prefix + self.alphabet[current_index])
                current_index += 1
            result.append(prefix + self.alphabet[current_index])
            prefix += char

        return result


s = Solution()

print(s.stringSequence("jk"))
print(s.stringSequence("abc"))
