class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #scan through array and keep track of fresh fruit count
        #multi source bfs on all rotting oranges, increment the time by 1 after appending 
        #neighbors and decrement fresh fruit count

        #return -1 if the fresh fruit count > 0 after q is empty

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh_cnt = 0
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                if row+1 < ROWS and grid[row+1][col] == 1:
                    fresh_cnt -= 1
                    grid[row+1][col] = 2
                    q.append((row+1,col))
                if row-1 >= 0 and grid[row-1][col] == 1:
                    fresh_cnt -= 1
                    grid[row-1][col] = 2
                    q.append((row-1,col))
                if col+1 < COLS and grid[row][col+1] == 1:
                    fresh_cnt -= 1
                    grid[row][col+1] = 2
                    q.append((row,col+1))
                if col-1 >= 0 and grid[row][col-1] == 1:
                    fresh_cnt -= 1
                    grid[row][col-1] = 2
                    q.append((row,col-1))
            time += 1

        if fresh_cnt > 0:
            return -1
        
        return max(0,time-1)







