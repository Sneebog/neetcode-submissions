class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # loop through
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1) ]
        ROWS, COLS = len(board),len(board[0])

        def dfs(r,c, flag):
            if r in range(0, ROWS) and c in range(0, COLS) and (r,c) not in visited and board[r][c] == "O":
                visited.add((r,c))
                if not flag or r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    flag = False
                else:
                    modify.append((r,c))

                for dr, dc in directions:
                    tmp_r, tmp_c = r + dr, c + dc
                    dfs(tmp_r, tmp_c, flag)
            return 

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and board[r][c] == "O":
                    modify = []
                    len_v = len(visited)
                    dfs(r,c, True)
                    if len_v + len(modify) == len(visited):
                        for up_r, up_c in modify:
                            board[up_r][up_c] = "X"
        return 
