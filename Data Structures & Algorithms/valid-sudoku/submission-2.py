class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row_set = set()
            col_set = set()
            grid_set = set()

            #col
            for col in range(0, 9):
                if board[col][i] != ".":
                    if board[col][i] in col_set:
                        return False
                    else:
                        col_set.add(board[col][i])
                    
            #row
            for row in range(0, 9):
                if board[i][row] != ".":
                    if board[i][row] in row_set:
                        return False
                    else:
                        row_set.add(board[i][row])
    

            #small_grid
            row_grid = (i // 3) * 3
            col_grid = (i % 3) * 3
            for grid_row_val in range(0,3):
                for grid_col_val in range(0,3):
                    row = row_grid + grid_row_val
                    col = col_grid + grid_col_val
                    if board[col][row] != ".":
                        if board[col][row] in grid_set:
                            return False
                        else:
                            grid_set.add(board[col][row])

        return True
