class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if they set values overlap combine them?
        #each set has positions
        islands = []

        #im just going loop through and merge if they meet
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(0, ROWS):
            for c in range(0, COLS):
                #check each island
                if grid[r][c] == "1":
                    island = set()
                    island.add((r,c))
                    tmp_islands = []
                    for i in range(0, len(islands)):
                        if (r+1,c) in islands[i] or (r-1,c) in islands[i] or (r,c+ 1) in islands[i] or (r,c - 1) in islands[i]:
                            val = islands[i]
                            island = island | val
                        else:
                            tmp_islands.append(islands[i])
                    tmp_islands.append(island)
                    islands = tmp_islands
        return len(islands)