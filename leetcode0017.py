class Solution:
    def __init__(self):
        self.temp = ""
        self.combos: list = []
        self.key_map: dict = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

    def combinations(self, digits):
        if not digits:
            self.combos.append(self.temp)
            return

        words = self.key_map[digits[-1]]
        for w in words:
            self.temp += w
            self.combinations(digits[:-1])
            self.temp = self.temp[:-1]

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return self.combos

        self.combinations(list(digits[::-1]))
        return self.combos


s = Solution()
print(s.letterCombinations("23"))


# from itertools import product

# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         if not digits:
#             return []

#         key_map = {
#             "2": "abc", "3": "def",
#             "4": "ghi", "5": "jkl",
#             "6": "mno", "7": "pqrs",
#             "8": "tuv", "9": "wxyz"
#         }

#         # Generate all combinations using cartesian product
#         char_lists = [key_map[d] for d in digits]
#         return ["".join(combo) for combo in product(*char_lists)]
