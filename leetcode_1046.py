import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert stones into a max heap by pushing negative values
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Get the two heaviest stones
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            # If they are not the same, push the difference back
            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))

        # If a stone remains, return it; otherwise, return 0
        return -stones[0] if stones else 0




s = Solution()

print(s.lastStoneWeight(stones = [2,7,4,1,8,1]))
