class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row to make sure theres nothing in seen dict
        #check each column to make sure theres nothing in seen dict
        #manually check each square to make sure theres nothing in seen dict

        for i in range(len(board)):
            seen_row = {}
            seen_col = {}
            for j in range(len(board[i])):

                if board[i][j] != "." and board[i][j] in seen_row:
                    return False
                else:
                    seen_row[board[i][j]] = 1

                if board[j][i] != "." and board[j][i] in seen_col:
                    return False
                else:
                    seen_col[board[j][i]] = 1

        seen_TL = {}
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] != "." and board[i][j] in seen_TL:
                    return False
                else:
                    seen_TL[board[i][j]] = 1
        
        seen_TM = {}
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] != "." and board[i][j] in seen_TM:
                    return False
                else:
                    seen_TM[board[i][j]] = 1
        
        seen_TR = {}
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] != "." and board[i][j] in seen_TR:
                    return False
                else:
                    seen_TR[board[i][j]] = 1
        
        seen_ML = {}
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] != "." and board[i][j] in seen_ML:
                    return False
                else:
                    seen_ML[board[i][j]] = 1
        
        seen_MM = {}
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] != "." and board[i][j] in seen_MM:
                    return False
                else:
                    seen_MM[board[i][j]] = 1
        
        seen_MR = {}
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] != "." and board[i][j] in seen_MR:
                    return False
                else:
                    seen_MR[board[i][j]] = 1

        seen_BL = {}
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] != "." and board[i][j] in seen_BL:
                    return False
                else:
                    seen_BL[board[i][j]] = 1
        
        seen_BM = {}
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != "." and board[i][j] in seen_BM:
                    return False
                else:
                    seen_BM[board[i][j]] = 1

        seen_BR = {}
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != "." and board[i][j] in seen_BR:
                    return False
                else:
                    seen_BR[board[i][j]] = 1

        return True
        


