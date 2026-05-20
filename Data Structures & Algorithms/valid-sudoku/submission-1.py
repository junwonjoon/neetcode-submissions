class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row validity
        columns = [[],[],[],[],[],[],[],[],[]]
        mini_squares = [[],[],[],[],[],[],[],[],[]]
        mini_square_index = -1
        column_index = 0
        for row in board:
            if is_valid(row):
                for index in range(len(row)):
                    columns[index].append(row[index])
            else:
                return False
        #check column validity
        for column in columns:
            if not is_valid(column):
                return False
        #Creating Minisquare
        for i in range(9):
            for j in range(9):
                if j < 3:
                    mini_squares[mini_square_index + 0].append(board[i][j])
                elif j < 6:
                    mini_squares[mini_square_index + 1].append(board[i][j])
                else:
                    mini_squares[mini_square_index + 2].append(board[i][j])
            if i != 0 and i % 3 == 2:
                mini_square_index += 3
           
        print(columns)
        print(mini_squares)
        for mini_square in mini_squares:
            if not is_valid(mini_square):
                return False
        return True

def is_valid(str_nums: List[str]) -> bool:
        valid = ["1","2","3","4","5","6","7","8", "9", "."]
        for str_num in str_nums:
            if str_num == ".":
                continue
            if str_num not in valid:
                return False
            valid.remove(str_num)
        return True
