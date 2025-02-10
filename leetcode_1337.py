import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # Compute (number of soldiers, row index) pairs
        soldier_counts = [(sum(row), i)
                          for i, row in enumerate(mat)]

        # Get the k weakest rows using a min-heap
        return [index for _, index in heapq.nsmallest(k, soldier_counts)]


s = Solution()
print(s.kWeakestRows(mat=[[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]], k=3))
