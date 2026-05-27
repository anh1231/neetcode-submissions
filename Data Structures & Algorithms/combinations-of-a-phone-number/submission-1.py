class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_let = {2:['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4:['g', 'h', 'i']\
                    , 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's']\
                    , 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']
        }

        res = []
        def dfs(i, cur):
            if i >= len(digits):
                if cur:
                    res.append(cur)
                return
            
            for j in num_let[int(digits[i])]:
                dfs(i+1, cur + j)
        dfs(0, '')
        return res