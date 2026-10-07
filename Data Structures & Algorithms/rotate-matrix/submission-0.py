class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        len_row = len(matrix[0])
        len_col = len(matrix)
        row_for_a = 0
        tmps = []
        for _ in range(len_col):
            tmp = []
            for i in range(len_row - 1, -1, -1):
                tmp.append(matrix[i].pop(0))
            tmps.append(tmp)
        for i in range(len_row):
            matrix[i] += tmps[i]

