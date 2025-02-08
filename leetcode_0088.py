class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if not nums1:
            nums1[:] = nums2
            return
        if not nums2:
            return

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                pointer = p2
                for i in range(p2 + 1, n):
                    if nums2[pointer] > nums2[i]:
                        nums2[pointer], nums2[i] = nums2[i], nums2[pointer]
                        pointer = i
                        

            p1 += 1

        for i in range(m, n+m):
            nums1[i] = nums2[p2]
            p2 += 1

        return nums1


s = Solution()

# print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(s.merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3))
# print(s.merge(nums1=[1], m=1, nums2=[], n=0))
# print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
