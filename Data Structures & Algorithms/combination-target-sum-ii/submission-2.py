class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target and cur not in res:
                res.append(cur.copy())
                return
            if i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                if total + candidates[j] > target:
                    break
                
                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()
        dfs(0, [], 0)
        return res