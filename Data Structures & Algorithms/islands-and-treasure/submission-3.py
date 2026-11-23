from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #run bfs from each treasure chest at the same time  
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        inf = 2**31-1
        #queue holds, cords and distance from treasure chest 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        
        while queue:
            r,c,d = queue.popleft()
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r+dr, c+dc 
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if grid[nr][nc] == inf:
                        queue.append((nr,nc,d+1))
                        grid[nr][nc] = d+1
            
