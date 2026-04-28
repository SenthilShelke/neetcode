class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        arr = []
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        if inserted == False:
            intervals.append(newInterval)

        res = []
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
            else:
                if intervals[i][0] <= res[-1][1]:
                    if intervals[i][1] > res[-1][1]:
                        res[-1][1] = intervals[i][1]
                else:
                    res.append(intervals[i])

        intervals = res
        return intervals

