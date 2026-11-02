class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #points[i] = [xi, yi]
        #minheap problem

        #(distance, x, y)
        minHeap = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap,(distance,x,y))
        
        res = []
        for i in range(k):
            #pop from the heap and add to res to return
            d, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res