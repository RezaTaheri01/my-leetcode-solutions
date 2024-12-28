class Solution:
    def distMoney(self, money: int, children: int) -> int:
        counter_8_dollar: int = 0

        # give each children 1 dollar at first
        money -= children
        if money < 0:
            return -1

        # check for 7 dollars and prevent 4 dollars
        for child in range(children):
            if money == 7 or ((money > 7 and children > 1) and (money != 10 or children > 2)):
                money -= 7
                children -= 1
                counter_8_dollar += 1

        return counter_8_dollar


s = Solution()
print(s.distMoney(20, 3))
print(s.distMoney(13, 3))
print(s.distMoney(17, 2))
