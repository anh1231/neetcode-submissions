class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for start, end in sorted(tickets)[::-1]:
            adj[start].append(end)
        
        res = []
        
        def dfs(node):
            while adj[node]:
                end = adj[node].pop()
                dfs(end)
            res.append(node)
        
        dfs('JFK')
        return res[::-1]