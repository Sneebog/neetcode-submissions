class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
      
      edgemap = [[] for i in range(n)]
      for e1, e2 in edges:
        edgemap[e1].append(e2)
        edgemap[e2].append(e1)
      res = 0
      
      def dfs(node, par):
        if node in graph:
          return 

        graph.add(node)
        for edge in edgemap[node]:
          if edge == par:
            continue
          dfs(edge, node)
        return
        
      graph = set()
      for node in range(0, n):
        if node not in graph:
          dfs(node, -1)
          res += 1
      return res