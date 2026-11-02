class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #run prims algo
        #start = (0,0)
        #(weight,index)

        visited = set()
        minHeap = [(0,0)]
        res = 0

        while len(visited) != len(points):
            #calculate all the distances from popped node
            weight, ind = heapq.heappop(minHeap)
            if ind in visited:
                continue
            res += weight
            visited.add(ind)
            for i in range(len(points)):
                if i == ind or i in visited:
                    continue
                weight = abs(points[ind][0] - points[i][0]) + abs(points[ind][1] - points[i][1])
                heapq.heappush(minHeap, (weight,i))
            
        return res





