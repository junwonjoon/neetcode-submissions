class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = True, False, False, False
        ans = []
        reverse = 1
        while matrix:
            if top:
                curr = matrix.pop(0)
                for elem in curr:
                    ans.append(elem)
                top = False
                right = True
            elif right:
                for row in matrix:
                    ans.append(row.pop())
                right = False
                bottom = True
            elif bottom:
                curr = matrix.pop()
                for elem in row[::-1]:
                    ans.append(elem)
                bottom = False
                left = True
            elif left:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
                left = False
                top = True
            temp = []
            for row in matrix:
                if row:
                    temp.append(row)
            matrix = temp
        return ans