class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
      edgemap = {i:[]  for i in range(n)}
      for n1, n2 in edges:
        edgemap[n1].append(n2)
        edgemap[n2].append(n1)

      tree = set()
      def dfs(node, par):
        #check if there is a cycle using the set 
        if node in tree:
          return False
        
        #no edges
        tree.add(node)
        for edge in edgemap[node]:
          if edge == par:
            continue
          if not dfs(edge, node): 
            return False

        return True
      return dfs(0, -1) and len(tree) == n