class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row,col):
            if row > ROWS-1 or row < 0:
                return 0
            if col > COLS-1 or col < 0:
                return 0
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return 1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))

        return res