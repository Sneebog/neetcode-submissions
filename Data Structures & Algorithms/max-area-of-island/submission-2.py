class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        #same as find the number of islands but with max length
        def bfs(r,c):
            area = 1
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                r, c = q.popleft()
                for dr , dc in directions:
                    new_r, new_c = r+ dr, c + dc
                    if new_r in range(ROWS) and new_c in range(COLS) and (new_r,new_c) not in visited and grid[new_r][new_c] == 1:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        area += 1
            return area

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 1 and (r,c) not in visited:

                    res = max(bfs(r,c), res)

        return res


