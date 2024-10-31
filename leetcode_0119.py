class Solution:  # O(n^2)
    def getRow(self, rowIndex: int) -> list[list[int]]:
        rowIndex += 1  # rowIndex start from 0 but my code is base on 1
        row_len = 2  # current level(deepness) that also current size

        # Edge cases
        if rowIndex < 3:
            return [1 for _ in range(rowIndex)]

        # Main Process
        prev = [1, 1]  # last row
        temp = []
        while row_len < rowIndex:
            row_len += 1

            for i in range(row_len):
                if i == 0 or i == row_len - 1:
                    temp.append(1)
                else:
                    temp.append(prev[i-1] + prev[i])
            prev = temp
            temp = []

        return prev


s = Solution()
print(s.getRow(5))


# The k-th element in the n-th row of Pascal’s Triangle is given by:
#    n!
# __________
#  K!(n-k)!

# class Solution:
#     def getRow(self, rowIndex: int) -> list[int]:
#         row = [1]  # The first element is always 1
        
#         # Generate each element based on the previous one
#         for k in range(1, rowIndex + 1):
#             # Calculate the next element in the row
#             next_value = row[-1] * (rowIndex - k + 1) // k
#             row.append(next_value)
        
#         return row
