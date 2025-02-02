class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # 1. O(n)
        # nums[i] != nums[i + 1] for all valid i.
        # return nums.index(max(nums))

        # 2. O(n)
        # l = len(nums)
        # if l == 1:
        #     return 0

        # for i in range(l):
        #     if (i - 1 < 0 or nums[i] > nums[i - 1]) and i + 1 > l - 1 or nums[i] > nums[i + 1]:
        #         return i

        # return -1  # Not found

        # 3. O(log n)
        # https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
        # If an element is smaller than it’s next element then it is guaranteed
        # that at least one peak element will exist on the right side of this element.

        # Conversely if an element is smaller than it’s previous element then it
        # is guaranteed that at least one peak element will exist on the left side of this element.

        n = len(nums)

        # If there is only one element, then it's a peak
        if n == 1:
            return 0

        # Check if the first element is a peak
        if nums[0] > nums[1]:
            return 0

        # Check if the last element is a peak
        if nums[-1] > nums[-2]:
            return n - 1
        
        left, right = 1, len(nums) - 2

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


s = Solution()

print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 3, 4, 8, 6, 7]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(s.findPeakElement([1,2,3,4,3]))
