class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)
        p_left, p_right = (0, length - 1)

        while p_left < p_right:
            Sum = numbers[p_left] + numbers[p_right]
            if Sum > target:
                p_right -= 1
            elif Sum == target:
                return [p_left+1, p_right+1]
            else:
                p_left += 1


s = Solution()
print(s.twoSum([2, 7, 11, 13], 9))
