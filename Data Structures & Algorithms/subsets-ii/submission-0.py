class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur):
            res.append(cur[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return res