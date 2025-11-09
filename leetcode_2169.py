class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op_counter = 0

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                c = num1 // num2
                num1 -= (c * num2)
            else:
                c = num2 // num1
                num2 -= (c * num1)
            op_counter += c

        return op_counter
