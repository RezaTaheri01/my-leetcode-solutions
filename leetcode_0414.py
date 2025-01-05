class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # without set or sort
        maximum = [float('-inf')] * 3

        for num in nums:  # O(n * 6)
            for i in range(3):
                if maximum[i] == num:
                    break
                if maximum[i] < num:
                    tmp, maximum[i] = maximum[i], num
                    # shift others
                    for j in range(i+1, 3):
                        tmp, maximum[j] = maximum[j], tmp
                    break

        return maximum[-1] if maximum[-1] != float('-inf') else maximum[0]


# class Solution:
#     def thirdMax(self, nums: list[int]) -> int:
#         nums.sort() # O(n.log n)

#         counter: int = 0
#         prev = nums[-1]
#         for num in reversed(nums):
#             if prev != num:
#                 counter += 1
#                 if counter == 2:
#                     return num
#             prev = num

#         return nums[-1]


s = Solution()
print(s.thirdMax(nums=[2, 2, 1, 1, 3]))
print(s.thirdMax(nums=[1, 2]))
print(s.thirdMax(nums=[3, 2, 1]))
print(s.thirdMax(nums=[1, 2, 2, 5, 3, 5]))
print(s.thirdMax(nums=[-3, -2, -1, 0]))
