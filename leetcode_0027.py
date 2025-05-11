class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wp = 0

        for num in nums:
            if num != val:
                nums[wp] = num
                wp += 1

        return wp
