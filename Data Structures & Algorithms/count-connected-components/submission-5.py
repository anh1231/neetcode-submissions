class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        comp = 0

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for i in adj[node]:
                if i != par and not dfs(i, node):
                    continue
            

        for i in range(n):
            if i not in visit:
                dfs(i, adj[i])
                comp += 1
        return comp