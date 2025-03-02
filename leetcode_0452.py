class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sort the intervals by the end points
        points.sort(key=lambda x: x[1])
        
        arrow = 1
        end = points[0][1]
        
        for start, stop in points[1:]:
            if end < start:
                arrow += 1
                end = stop
                
        return arrow



s = Solution()

print(s.findMinArrowShots([[10, 16], [2, 10], [1, 6], [7, 12]]))
print(s.findMinArrowShots([[1, 6], [2, 10], [7, 12], [10, 16]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[-1, 1], [0, 1], [2, 3], [1, 2]]))
print(s.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
