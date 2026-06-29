class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #make prerequisites map
        prevMap = {i:[] for i in range(numCourses)}
        for cour, prev in prerequisites:
            prevMap[cour].append(prev)
        visited = set()
        valid = set()
        ver = []
        res = []
        #do dfs
        def dfs(cour):
          #base case if its in visited set break:
          if cour in visited: 
            return False
          #else if in valid set?  
          if cour in valid and cour not in visited:
            return True

          visited.add(cour)
          for prev in prevMap[cour]:
              if not dfs(prev):
                return False
          valid.add(cour)
          visited.remove(cour)
          res.append(cour)
          return True
        #make a true loop
        for cour in range(numCourses):
          if not dfs(cour):
            return []
        return res
