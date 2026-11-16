class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r,c):
            #return if (r,c) in memo
            if (r,c) in memo:
                return memo[(r,c)]
            
            #best should just be 1 because you always have max length of 1 (start)
            best = 1
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr,nc))
            
            #gotten best path so put it in memo
            memo[(r,c)] = best
            return best 

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))
        
        return res