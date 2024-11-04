class Solution:  # best in runtime speed
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        # remove duplicates
        nums1 = set(nums1)
        nums2 = set(nums2)

        for num in nums2:  # O(n)
            if num in nums1:  # O(1)
                result.append(num)
        return result


class Solution2:  # best in memory usage
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        seen = {}

        # remove duplicates nums1
        for n in nums1:  # O(n)
            seen[n] = True

        for num in nums2:  # O(n)
            if num in nums1 and seen[num]:  # O(1)
                result.append(num)
                seen[num] = False

        return result


s = Solution()
s2 = Solution()
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(s2.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
