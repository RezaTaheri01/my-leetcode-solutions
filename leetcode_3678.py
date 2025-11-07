class Solution:
    def smallestAbsent(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        avg = sum(nums) / len(nums)
        nums = sorted(set(nums))
        n = len(nums)

        if avg < 0:
            avg = 0

        # Binary search for first number > avg
        left, right = 0, n
        while left < right:            
            mid = (left + right) // 2
            if nums[mid] > avg:
                right = mid - 1
            else:
                left = mid + 1

        # left is now the first index with nums[left] > avg, or n if none
        sap = int(avg) + 1
        while left < n:
            if sap < nums[left]:
                break
            elif sap == nums[left]:
                sap += 1
            left += 1

        return sap


s = Solution()
print(s.smallestAbsent(nums=[-100, 0, 0, 0]))
print(s.smallestAbsent(nums=[3, 3, 3, 3]))
print(s.smallestAbsent(nums=[4, -1]))
print(s.smallestAbsent(nums=[3, 5]))
print(s.smallestAbsent(nums = [-5, -1, 0, 2]))
print(s.smallestAbsent(nums = [10, 20, 30]))


