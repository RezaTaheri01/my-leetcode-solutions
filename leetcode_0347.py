from typing import List
from collections import Counter
import heapq


class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        frequency_heap = []
        for num, freq in counter.items():
            heapq.heappush(frequency_heap, (freq, num))

        topK = heapq.nlargest(k, frequency_heap)

        return [num for _, num in topK]
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]


s = Solution()

print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(s.topKFrequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2))
