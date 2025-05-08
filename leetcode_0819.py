class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph += "."
        banned = set(banned)

        # find words and remove banned
        temp: str = ""
        word_list: list[str] = []
        for char in paragraph:
            if not char.isalpha():
                if temp and temp.lower() not in banned:
                    word_list.append(temp.lower())
                temp = ""
            else:
                temp += char

        # count word repeats and find the most repeated one
        max, target = 0, ""
        for word in word_list:
            temp = word_list.count(word)
            if max < temp:
                target = word
                max = temp

        return target