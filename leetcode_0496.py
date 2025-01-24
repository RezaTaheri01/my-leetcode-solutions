from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map: dict = {}  # O(n) space

        for i in range(len(nums2)-1):  # O(n^2) 
            j = i + 1
            while j < len(nums2):
                if nums2[i] < nums2[j]:
                    next_greater_map[nums2[i]] = nums2[j]
                    break
                j += 1

        for i in range(len(nums1)):  # O(m)
            nums1[i] = next_greater_map.get(nums1[i]) or -1

        return nums1


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
print(s.nextGreaterElement(nums1=[], nums2=[]))
print(s.nextGreaterElement(nums1=[1,3,5,2,4], nums2=[6,5,4,3,2,1,7]))
