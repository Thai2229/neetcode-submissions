"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by start times
        #then if the end time of the first <= start time of next its valid
        #else not

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True

        