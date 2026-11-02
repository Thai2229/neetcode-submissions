class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #loop from bottom to top for each column, append to a new row
        res = []
        
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):    
                row.append(matrix[j][i])
            res.append(row[::-1])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = res[i][j]