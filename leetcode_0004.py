# Todo: O(log (m+n))
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1 += nums2
    nums1.sort()
     
    if nums1:
        l = len(nums1)
        if l % 2 == 0:
            return (nums1[l//2] + nums1[l//2 - 1]) / 2
        else:
            return nums1[l//2]


print(findMedianSortedArrays([1,2], [4,3]))