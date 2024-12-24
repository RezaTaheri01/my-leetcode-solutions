class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # define two dictionary to convert str to int and vice versa
        str_to_int: dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        int_to_str: dict = dict()
        for key, value in str_to_int.items():  # reverse key, value of str_to_int
            int_to_str[value] = key

        # equal the length of num1 & num2 by zero and add one extra zero
        target_len = max(len(num1), len(num2)) + 1
        num1 = num1.zfill(target_len)
        num2 = num2.zfill(target_len)

        result: str = ""
        next_add = 0
        for i in range(target_len - 1, -1, -1):
            temp = str_to_int[num1[i]] + str_to_int[num2[i]] + next_add

            if temp >= 10:
                next_add = temp // 10
                temp %= 10
            else:
                next_add = 0

            result = int_to_str[temp] + result

        # remove extra zero if founded and return result
        return result[1:] if result[0] == "0" else result


s = Solution()
print(s.addStrings("999", "201"))
