from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize the domino
            hashmap[key] = hashmap.get(key, 0) + 1

        for value in hashmap.values():
            result += value * (value - 1) // 2

        return result


s = Solution()
print(s.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [5, 6], [4, 3]]))  # 1

print(s.numEquivDominoPairs(
    dominoes=[[1, 2], [2, 1], [3, 4], [5, 6], [4, 3]]))  # 2

print(s.numEquivDominoPairs(
    dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))  # 3
