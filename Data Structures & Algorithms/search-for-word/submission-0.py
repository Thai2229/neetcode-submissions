class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(row, col, curr_word):
            if curr_word == word:
                return True

            if len(curr_word) >= len(word):
                return False

            visited.add((row, col))

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < ROWS and 
                    0 <= new_col < COLS and
                    (new_row, new_col) not in visited):

                    if board[new_row][new_col] == word[len(curr_word)]:
                        if dfs(new_row, new_col, curr_word + board[new_row][new_col]):
                            return True

            visited.remove((row, col))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[0]):
                        return True

        return False