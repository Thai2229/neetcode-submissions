import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Sort queries while preserving original indices
        dummy = sorted(enumerate(queries), key=lambda x: x[1])

        min_heap = []
        # (size, right)

        res = [0] * len(queries)

        # i for intervals, j for queries
        i, j = 0, 0

        while j < len(dummy):
            original_index, query = dummy[j]

            # Push intervals whose start <= query
            while i < len(intervals) and query >= intervals[i][0]:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (length, intervals[i][1]))
                i += 1

            # Pop intervals whose end < query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # Store answer at original query index
            if min_heap:
                res[original_index] = min_heap[0][0]
            else:
                res[original_index] = -1

            j += 1

        return res