class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0 

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr in range(0, ROWS)) and (c + dc in range(0, COLS)) and grid[r + dr][c + dc] == "1" and (r + dr,c + dc) not in visited:
                        q.append((r + dr,c + dc))
                        visited.add((r + dr,c + dc))
            return 



        for r in range(0, ROWS):
            for c in range(0,COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands