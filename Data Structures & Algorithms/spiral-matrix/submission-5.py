class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, right = True, True
        ans = []
        reverse = 1
        while matrix:
            if top and right:
                curr = matrix.pop(0)
                for elem in curr:
                    ans.append(elem)
                top = False
            elif right:
                for row in matrix:
                    ans.append(row.pop())
                right = False
            elif not top:
                curr = matrix.pop()
                for elem in reversed(row):
                    ans.append(elem)
                top = True
            elif not right:
                for row in reversed(matrix):
                    ans.append(row.pop(0))
                right = True
            temp = []
            for row in matrix:
                if row:
                    temp.append(row)
            matrix = temp
        return ans