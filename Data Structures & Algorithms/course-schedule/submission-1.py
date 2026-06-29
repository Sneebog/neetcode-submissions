class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #have a prev map
        prevMap = {i:[] for i in range(numCourses)}
        for curs , prev in prerequisites:
          prevMap[curs].append(prev)
        visited = set()
        #dfs though each node
        def dfs(curs):
          if curs in visited:
            return False
          if not prevMap[curs]:
            return True
          visited.add(curs)
          for prev in prevMap[curs]:
            if not dfs(prev): return False
          visited.remove(curs)
          prevMap[curs] = []
          return True
        # if any aren't valid return false
        #loop through all the nodes?
        for node in range(numCourses ):
          if not dfs(node): return False
        return True
