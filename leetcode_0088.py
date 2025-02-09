class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p, p1, p2 = m + n - 1, m - 1, n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements, copy them over
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]

        return nums1  # Not necessary, since nums1 is modified in-place


s = Solution()

print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(s.merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3))
print(s.merge(nums1=[1], m=1, nums2=[], n=0))
print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
