class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #get a map of all prerequisites
        prevMap  = {i:[] for i in range(0, numCourses)}
        
        for crs, prev in prerequisites:
            prevMap[crs].append(prev)
        #dfs through them
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prevMap[crs] == []:
                return True
            
            visited.add(crs)
            for prev in prevMap[crs]:
                if not dfs(prev): return False
            visited.remove(crs)
            prevMap[crs] = []
            return True
        #loop through all the nodes
        for i in range(0, numCourses):
            print(i)
            if not dfs(i):
                return False
        return True