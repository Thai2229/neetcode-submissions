class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #need to sort intervals by start, then same as insert interval logic 

        intervals.sort(key=lambda x: (x[0], x[1]))

        res = []
        curr = intervals[0]

        for i in range(len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            elif curr[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                curr = [min(curr[0],intervals[i][0]), max(curr[1],intervals[i][1])]
        
        res.append(curr)
        return res