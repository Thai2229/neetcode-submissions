class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #run dfs from every "O" on the edge of the board, mark them as safe
        visited = set()
        ROWS,COLS = len(board), len(board[0])
        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in visited and
                    board[nr][nc] == "O"):

                    dfs(nr, nc, visited)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i == ROWS-1 or i == 0 or 
                j == 0 or j == COLS-1) and (i,j) not in visited:
                    dfs(i,j,visited)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        
