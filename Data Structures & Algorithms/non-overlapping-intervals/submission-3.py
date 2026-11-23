class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #always want to remove the interval that has the least 
        #ending i.e min(interval[1])

        intervals.sort(key=lambda x : (x[0], x[1]))

        res = 0
        curr = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0] < curr[1]:
                res += 1
                if intervals[i][1] < curr[1]:
                    curr = intervals[i]
            
            if intervals[i][0] >= curr[1]:
                curr = intervals[i]
        
        return res