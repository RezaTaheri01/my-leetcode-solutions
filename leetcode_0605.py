class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # it's better to remove padding for O(1) Space Complexity
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2))
