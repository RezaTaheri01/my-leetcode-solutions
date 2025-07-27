from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            if x + y < x + y:
                return 1
            return 0

        str_nums = list(map(lambda x: str(x), nums))

        # cmp_to_key() lets us use a comparison function for sorting
        str_nums.sort(key=cmp_to_key(compare))

        # Removing leading zeros
        if str_nums[0] == '0':
            return '0'

        return ''.join(str_nums)


s = Solution()
print(s.largestNumber(nums=[10, 2]))
print(s.largestNumber(nums=[20, 2]))
print(s.largestNumber(nums=[0, 0, 0]))
print(s.largestNumber(nums=[3, 39, 34, 303, 5, 9]))
print(s.largestNumber(nums=[1, 323, 4, 33]))
print(s.largestNumber(nums=[1, 3234545599999, 4, 33, 34]))
print(s.largestNumber(nums=[432, 43243]))
