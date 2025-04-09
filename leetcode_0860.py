# class Solution:
#     def lemonadeChange(self, bills: list[int]) -> bool:
#         lemonade_price = 5
#         change_in_hand: dict = {10:0, 5:0}

#         def payback(chng: int) -> bool:
#             for money in change_in_hand.keys():
#                 if chng >= money:
#                     cash_count = chng // money
#                     if cash_count <= change_in_hand[money]:
#                         change_in_hand[money] -= cash_count
#                         chng -= cash_count * money

#             return chng == 0

#         for cus_cash in bills:
#             change = cus_cash - lemonade_price

#             if change != 0 and not payback(change):
#                 return False

#             if cus_cash != 20:
#                 change_in_hand[cus_cash] += 1

#         return True


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change_in_hand = {5: 0, 10: 0}

        for cus_cash in bills:
            change = cus_cash - 5  # Calculate change needed

            if change == 15:
                # Try to give change with one $10 bill and one $5 bill if available
                if change_in_hand[10] > 0 and change_in_hand[5] > 0:
                    change_in_hand[10] -= 1
                    change_in_hand[5] -= 1
                elif change_in_hand[5] >= 3:
                    change_in_hand[5] -= 3
                else:
                    return False
            elif change == 5:
                # Try to give change with one $5 bill
                if change_in_hand[5] > 0:
                    change_in_hand[5] -= 1
                else:
                    return False

            # Update change_in_hand
            if cus_cash != 20:
                change_in_hand[cus_cash] += 1

        return True


s = Solution()

print(s.lemonadeChange(bills=[5, 5, 5, 10, 20]))
print(s.lemonadeChange(bills=[5, 5, 10, 10, 20]))
print(s.lemonadeChange(bills=[5, 5, 5, 20]))
