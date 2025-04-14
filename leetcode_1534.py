from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        counter = 0
        for i in range(l):
            for j in range(i + 1, l):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, l):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            counter += 1

        return counter


s = Solution()

print(s.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
