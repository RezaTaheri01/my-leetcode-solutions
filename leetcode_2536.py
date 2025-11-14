from typing import List
import numpy as np


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 1 <= queries.length <= 10 ^ 4
        mat = np.zeros(shape=(n, n), dtype=np.int16)

        for x1, y1, x2, y2 in queries:
            mat[x1: x2+1, y1: y2+1] += 1

        return mat.tolist()


s = Solution()

print(s.rangeAddQueries(n=3, queries=[[1, 1, 2, 2], [0, 0, 1, 1]]))
