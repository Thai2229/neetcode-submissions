class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t_bound, b_bound, l_bound, r_bound = 0, len(matrix)-1, 0, len(matrix[0])-1
        pointer = (0,0)
        res = []
        count = 0
        total = len(matrix)*len(matrix[0])

        while count < total:
            #right
            while pointer[1] <= r_bound and count < total:
                count += 1
                res.append(matrix[pointer[0]][pointer[1]])
                pointer = (pointer[0], pointer[1]+1)
            t_bound += 1
            pointer = (t_bound, r_bound)
            #down
            while pointer[0] <= b_bound and count < total:
                count += 1
                res.append(matrix[pointer[0]][pointer[1]])
                pointer = (pointer[0]+1, pointer[1])
            r_bound -= 1
            pointer = (b_bound, r_bound)
            #left
            while pointer[1] >= l_bound and count < total:
                count += 1
                res.append(matrix[pointer[0]][pointer[1]])
                pointer = (pointer[0], pointer[1]-1)
            b_bound -= 1
            pointer = (b_bound, l_bound)
            #up
            while pointer[0] >= t_bound and count < total:
                count += 1
                res.append(matrix[pointer[0]][pointer[1]])
                pointer = (pointer[0]-1, pointer[1])
            l_bound += 1
            pointer = (t_bound, l_bound)

        return res