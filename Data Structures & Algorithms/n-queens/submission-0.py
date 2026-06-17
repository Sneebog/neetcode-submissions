class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board  = [["."]* n for i in range(n)]
       
        #go row by row
        row = 0
        #check cols
        cols_set = set()
        #check pos diagonal
        pos_diag = set()
        #check neg diagonal
        neg_diag = set()

        def dfs(row, board):
            if row == n:
                res.append([row.copy() for row in board])
                return 
            
            for col in range(0, n):
                if col not in cols_set and row - col not in neg_diag and row + col not in pos_diag:
                    cols_set.add(col)
                    pos_diag.add( row + col)
                    neg_diag.add( row - col)
                    board[row][col] = 'Q'
                    dfs(row + 1, board)
                    board[row][col] = '.'
                    cols_set.remove(col)
                    pos_diag.remove( row + col)
                    neg_diag.remove( row - col)
           
        dfs(0, board)
        arr = []
        for board in res:
            tmp_b = []
            for row in board:
                tmp_row = ""
                for val in row:
                    tmp_row += val
                tmp_b.append(tmp_row)

            arr.append(tmp_b)
        return arr