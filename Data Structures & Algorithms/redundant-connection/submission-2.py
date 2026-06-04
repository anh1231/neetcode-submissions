class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n + 1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            
            visit.add(node)

            for i in adj[node]:
                if i == par:
                    continue
                if dfs(i, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []