class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visits = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visits:
                return False
            if preMap[crs] == []:
                return True
            
            visits.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
            visits.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True