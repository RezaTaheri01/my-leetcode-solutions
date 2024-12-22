# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool: pass  # Comment this part


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n  # Start from version 1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:  # not the edge, but still bad version
                    r = mid - 1
            else:  # mid is good version
                l = mid + 1

        return -1
