class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}
        # Count occurrences in the smaller list to save space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for n in nums1:  # O(n)
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        result = []

        for num in nums2:  # Iterate over nums2
            # Only add if num is in nums1 and still has counts left
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1  # Decrease the count

        return result


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
