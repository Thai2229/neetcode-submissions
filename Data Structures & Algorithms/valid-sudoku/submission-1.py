class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for r in range(9):
            seen = set()
            for c in range(9):
                v = board[r][c]
                if v != ".":
                    if v in seen: return False
                    seen.add(v)

        # cols
        for c in range(9):
            seen = set()
            for r in range(9):
                v = board[r][c]
                if v != ".":
                    if v in seen: return False
                    seen.add(v)

        # boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        v = board[r][c]
                        if v != ".":
                            if v in seen: return False
                            seen.add(v)

        return True
