class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #run dfs whenever you find a 1, make sure to change that 1 to a 0
        #so you don't overcount, add to the total island count
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row,col):
            if row > ROWS-1 or row < 0:
                return 
            if col > COLS-1 or col < 0:
                return 
            if grid[row][col] == "0":
                return 
            
            grid[row][col] = "0"
            dfs(row+1,col) 
            dfs(row-1,col) 
            dfs(row,col+1) 
            dfs(row,col-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)

        return res