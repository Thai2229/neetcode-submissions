"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #need to track the earliest end time, if curr interval start > 
        #earliest end time then don't add another room, else, need to add 
        #another room 

        intervals.sort(key=lambda x: x.start) 

        res = 0
        min_heap = []

        for interval in intervals:
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,interval.end)
            else:
                res += 1
                heapq.heappush(min_heap,interval.end)

        return res






