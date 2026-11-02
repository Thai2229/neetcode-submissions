from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi-source BFS: start from all treasure chests at once
        # Only update a cell if it is INF

        INF = 2**31 - 1
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            # Check all 4 possible positions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                # Check bounds and make sure the cell is unvisited land
                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF):

                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))