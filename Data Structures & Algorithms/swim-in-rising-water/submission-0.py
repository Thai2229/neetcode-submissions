class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #want to optimze: find the path that has the lowest highest elevation possible
        #use dijkstras to optimize this, instead of taking the path with the lowest weight
        #take the path with the lowest altitude

        #minheap = highest elevation seen, row, col
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()

        while True:
            height, row, col = heapq.heappop(minHeap)
            if (row,col) in visited:
                continue
            visited.add((row,col))
            #if you reach the end, break and return
            if row == len(grid)-1 and col == len(grid)-1: 
                return height
            #potential new candidates
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid):
                    heapq.heappush(minHeap, (max(grid[nr][nc],height), nr, nc))
                

            


            