
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        preMap = [[] for i in range(n)]

        for a,b in edges:
            preMap[a].append(b)
            preMap[b].append(a)
        
        q = deque([[0,-1]])
        visit = set()

        while q:
            node, par = q.popleft()
            if node in visit:
                return False
            
            visit.add(node)
            for i in preMap[node]:
                if i != par:
                    q.append([i, node])
        return True and len(visit) == n
        