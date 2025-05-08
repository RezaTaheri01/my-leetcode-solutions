from typing import List


# All the values of heights are distinct.
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = {heights[i]: names[i] for i in range(len(heights))}

        heights.sort(reverse=True)

        for i in range(len(heights)):
            names[i] = name_height[heights[i]]

        return names


s = Solution()

print(s.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(s.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))
