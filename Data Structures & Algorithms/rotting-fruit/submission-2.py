class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS,COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fruit = set()
        #loop through and find rotten fruit positions
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    fruit.add((r,c))
                if grid[r][c] == 1:
                    fruit.add((r,c))
        #add to queue and bfs it 
        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for i in range(0, len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    tmp_r, tmp_c = r + dr, c + dc
                    if tmp_r in range(ROWS) and tmp_c in range(COLS) and (tmp_r,tmp_c) not in visited and grid[tmp_r][tmp_c] == 1:
                        q.append((tmp_r,tmp_c))
                        visited.add((tmp_r,tmp_c))
            time += 1
        if time != 0:
            time -= 1
        #with time essentially

        #return final time
        return time if visited == fruit else -1