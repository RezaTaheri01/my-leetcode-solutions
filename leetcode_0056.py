from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort base on first element on each inner list
        intervals.sort()
        
        # reverse list
        intervals.reverse()
        
        # iterate from end
        for i in range(len(intervals) - 1, -1, -1):
            if i != 0:
                if intervals[i][1] >= intervals[i-1][0]:
                    ... # two list can be merged
                    if intervals[i][1] > intervals[i-1][1]:
                        intervals[i-1][1] = intervals[i][1]
                    if intervals[i][0] < intervals[i-1][0]:
                        intervals[i-1][0] = intervals[i][0]

                    intervals.pop(i)

        return intervals[::-1]


s = Solution()
print(s.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))