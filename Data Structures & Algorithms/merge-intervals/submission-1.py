class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []

        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[0])
            else:
                if intervals[i][0] <= res[-1][1]:
                    if intervals[i][1] > res[-1][1]:
                        res[-1][1] = intervals[i][1]
                else:
                    res.append(intervals[i])

        return res
                    
