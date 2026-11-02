
import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  # Smaller half (negative numbers)
        self.minHeap = []  # Larger half

    def addNum(self, num: int) -> None:
        # Add to maxHeap first
        heapq.heappush(self.maxHeap, -num)

        # Make sure every number in maxHeap <= every number in minHeap
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        # Balance the heap sizes
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        elif len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        # Even number of elements
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
