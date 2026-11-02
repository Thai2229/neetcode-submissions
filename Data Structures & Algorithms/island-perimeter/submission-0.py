class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #for each 1, you check if square above, below, left, right is land
        #if so then - 1 from 4 total, since a piece can have a max perim of 4
        #else, don't; this includes water and just nothing
        
        res = 0
         
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1: 
                    perimeter = 4
                    #code for checking land perim here:
                    if col-1 >= 0 and grid[row][col-1] == 1:
                        perimeter -= 1
                    if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                        perimeter -= 1
                    if row+1 < len(grid) and grid[row+1][col] == 1:
                        perimeter -= 1
                    if row-1 >= 0 and grid[row-1][col] == 1:
                        perimeter -= 1

                    res += perimeter
        
        return res
                    
