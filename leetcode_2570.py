from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        results: list[list[int]] = []

        while p1 < l1 and p2 < l2:
            id1, id2 = nums1[p1][0], nums2[p2][0]
            if id1 == id2:
                results.append([id1, nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif id1 < id2:
                results.append(nums1[p1])
                p1 += 1
            else:
                results.append(nums2[p2])
                p2 += 1

        results.extend(nums1[p1:])
        results.extend(nums2[p2:])

        return results


s = Solution()
print(s.mergeArrays([[1, 2], [2, 3], [4, 5]],
                    [[1, 4], [3, 2], [4, 1]]))
