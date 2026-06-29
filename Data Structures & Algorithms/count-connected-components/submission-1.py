class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
      
      edgemap = [[] for i in range(n)]
      for e1, e2 in edges:
        edgemap[e1].append(e2)
        edgemap[e2].append(e1)
      res = []
      
      def dfs(node, par):
        if node in graph:
          return 

        graph.add(node)
        for edge in edgemap[node]:
          if edge == par:
            continue
          dfs(edge, node)
        return
      visited = set()
      for node in range(0, n):
        if node not in visited:
          graph = set()
          dfs(node, -1)
          res.append(graph)
          visited = visited | graph
      conn = 0
      # for graph in res:
      #   if len(graph) > 1:
      #     conn += 1
      return len(res)