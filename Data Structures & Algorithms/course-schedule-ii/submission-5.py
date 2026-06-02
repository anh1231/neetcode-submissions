class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for i in prerequisites:
            preMap[i[0]].append(i[1])


        res = []
        cycle, visits = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visits:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visits.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
