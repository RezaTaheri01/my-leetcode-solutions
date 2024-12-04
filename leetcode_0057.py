class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)

        # merge base on problem 56.Merge Intervals:
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
        