class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        ROWS, COLS = len(grid), len(grid[0])   
        q = deque()
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        while q:
            for i in range(0, len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    tmp_r, tmp_c = r + dr, c + dc
                    if tmp_r in range(ROWS) and tmp_c in range(COLS) and (tmp_r,tmp_c) not in visited and grid[tmp_r][tmp_c] != -1:
                        q.append((tmp_r,tmp_c))
                        visited.add((tmp_r,tmp_c))
            dist += 1
        return 