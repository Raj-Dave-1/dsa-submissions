class Solution:
    def checkSubBox(self, board: List[List[str]], row: int, col: int) -> bool:
        dic = {}
        
        for i in range(3):
            for j in range(3):
                val = board[row+i][col+j]
                if val != '.':
                    if val in dic:
                        return False
                    dic[val] = 1
        
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row wise
        for i in range(9):
            dicRow = {}
            dicCol = {}
            for j in range(9):
                valRow = board[i][j]
                if valRow != '.':
                    if valRow in dicRow:
                        return False
                    dicRow[valRow] = 1


                valCol = board[j][i]
                if valCol != '.': 
                    if valCol in dicCol:
                        return False
                    dicCol[valCol] = 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.checkSubBox(board, i, j) == False:
                    return False

        return True


            