class Solution:  # O(n^2)
    def generate(self, numRows: int) -> list[list[int]]:
        pascal: list = [[1], [1, 1]]  # init
        row_len = 2  # current level(deepness) that also current size

        # Edge cases
        if numRows < 3:
            return pascal[:numRows]

        # Main Process
        temp = []
        while row_len < numRows:
            row_len += 1

            for i in range(row_len):
                if i == 0 or i == row_len - 1:
                    temp.append(1)
                else:
                    temp.append(pascal[row_len-2][i-1] + pascal[row_len-2][i])

            pascal.append(temp)
            temp = []

        return pascal


def main():
    s = Solution()
    result = s.generate(5)
    print(result)


if __name__ == "__main__":
    main()


# The k-th element in the n-th row of Pascal’s Triangle is given by:

#    n!
# __________
#  K!(n-k)!