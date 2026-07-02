from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst_col_0 = [row[0] for row in matrix]
        row_to_look = bisect_left(lst_col_0, target)
        if row_to_look < len(matrix) and lst_col_0[row_to_look] == target:
            return True
        else:
            row_to_look -= 1
        index = bisect_left(matrix[row_to_look], target)
        if index < len(matrix[0]) and matrix[row_to_look][index] == target:
            return True
        else:
            return False
