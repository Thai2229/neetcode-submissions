class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #python only supports minheaps, get around this by using negative numbers
        maxHeap = [] #all negative nums btw

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            if first != second:
                heapq.heappush(maxHeap, -abs(first-second))
        
        if maxHeap:
            return -maxHeap[0]
        
        return 0