class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row_hashmap = {}
            col_hashmap = {}
            grid_hashmap = {}
            #col
            for col in range(0, 9):
                col_hashmap[board[col][i]] = col_hashmap.get(board[col][i], 0) + 1
                if col_hashmap[board[col][i]] > 1 and board[col][i] != "." :
                    return False
                    
            #row
            for row in range(0, 9):
                row_hashmap[board[i][row]] = row_hashmap.get(board[i][row], 0) + 1
                if row_hashmap[board[i][row]] > 1 and board[i][row] != "." :
                    return False

            #small_grid
            row_grid = (i // 3) * 3
            col_grid = (i % 3) * 3
            for grid_row_val in range(0,3):
                for grid_col_val in range(0,3):
                    row = row_grid + grid_row_val
                    col = col_grid + grid_col_val
                    grid_hashmap[board[col][row]]= grid_hashmap.get(board[col][row], 0) + 1
                    if grid_hashmap[board[col][row]] > 1 and board[col][row] != ".":
                        return False
        return True
