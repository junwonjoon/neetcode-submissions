from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_to_look = bisect_left([row[0] for row in matrix], target)
        if row_to_look < len(matrix) and matrix[row_to_look][0] == target:
            return True
        row_to_look -= 1
        index = bisect_left(matrix[row_to_look], target)
        if index < len(matrix[0]) and matrix[row_to_look][index] == target:
            return True
        return False
