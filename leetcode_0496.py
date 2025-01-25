from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map: dict = {}  # O(n) space
        stack: list[int] = []  # O(n) space

        # Iterate over nums2 to populate the next_greater_map
        for num in nums2:  # O(n)
            while stack and num > stack[-1]:
                next_greater_map[stack.pop()] = num

            stack.append(num)

        for i in range(len(nums1)):  # O(m)
            nums1[i] = next_greater_map.get(nums1[i]) or -1

        return nums1


s = Solution()

print(s.nextGreaterElement(nums1=[], nums2=[]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[1, 3, 5, 2, 4], nums2=[6, 5, 4, 3, 2, 1, 7]))
